# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

class HelloWorld:
    def say_hello(self, name):
        return 'Hello, ' + name

    def fibonacci(self, n):
        table = [0,1]
        
        for i in range(2,n+1):
            table.append(table[i-2] + table[i-1])

        return table[n]
