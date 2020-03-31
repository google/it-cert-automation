#!/usr/bin/env python3
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import heapq
import math
import os
import sys
import setproctitle

from concurrent import futures

import zimply
import zimply.zimply

from bs4 import BeautifulSoup


def html_text(content):
    soup = BeautifulSoup(content, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    return text


def generate_stats(words):
    heap = [
        (- amount, word, refs) for word, (amount, refs) in words.items()
    ]
    heapq.heapify(heap)

    for n_amount, word, refs in heapq.nsmallest(50, heap):
        amount = - n_amount
        print(f'{word} with {amount}')


def process_entries(worker_id, start, end):
    words = {}

    zim = zimply.zimply.ZIMFile('data.zim', 'utf-8')
    #print("Worker id: {} Handling: {} {}".format(worker_id, start, end))
    for i, idx in enumerate(range(start, end)):

        # pending = end - idx
        # if (i % 100) == 0:
        #     print(f'[{worker_id}]: {i}, pending: {pending}')

        try:
            article = zim._get_article_by_index(idx, follow_redirect=False)
            html_data = article.data
        except Exception:
            print(f'ERROR: in idx={idx}')
            continue

        if not html_data:
            continue

        text = html_text(html_data)

        for word in text.split():
            word = word.lower()
            value = words.setdefault(word, [0, set()])
            value[0] += 1
            value[1].add((idx, article.namespace, text))

    return words


setproctitle.setproctitle("contents_stats")

zim = zimply.zimply.ZIMFile('data.zim', 'utf-8')
#entry_count = len(zim)
entry_count = 100000
# nproc = os.cpu_count()
# entries_per_proc = int(max(1, math.ceil(entry_count / nproc)))
entries_per_proc = 100

words = {}

with futures.ProcessPoolExecutor() as executor:
    workers = set()

    for i, start in enumerate(
        range(0, entry_count, entries_per_proc)
    ):
        end = min(start + entries_per_proc, entry_count)
        # print(f'entries: {entry_count}, nproc: {nproc}, '
        #       f'start: {start}, end: {end}')
        #print("Adding {} worker".format(i))
        workers.add(executor.submit(process_entries, i, start, end))

    for task in futures.as_completed(workers):
        #print("Merging processed articles")
        article_words = task.result()
        # Merge the article words
        for word, (amount, refs) in article_words.items():
            value = words.setdefault(word, [0, set()])
            value[0] += amount
            value[1].update(refs)

generate_stats(words)

