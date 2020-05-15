# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

class HelloWorld:
    def say_hello(self, name):
        return 'Hello, ' + name

    def fibonacci(self, num):
        if num == 0:
            return 0
        elif num == 2 or num == 1:
            return 1
        else:
            return self.fibonacci(num - 2) + self.fibonacci(num - 1)
