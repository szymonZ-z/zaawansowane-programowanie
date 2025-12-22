from collections import Counter
import re

def is_palindrome(text: str):
    text = text.lower()
    text_list = []
    for char in text:
        if  'a' <= char <= 'z':
            text_list.append(char)
    for i in range(0 , len(text_list) // 2):
        if text_list[i] != text_list[len(text_list) -1 -i]:
            return False
    return True

def fibonacci(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2:
        return fibonacci(n - 1) + fibonacci(n - 2)
    return None

def count_vowels(text: str):
    return len(["ok" for c in text.lower() if c in ["a" , "e" , "i" , "o" ,"u" ,"y" , "ó"]])

def calculate_discount(price: float, discount: float):
    if discount < 0 or discount > 1:
        return ValueError
    return price * (1 - discount)

def flatten_list(nested_list: list):
    result_list = []
    for element in nested_list:
        print(type(element))
        if isinstance(element, list):
            result_list.extend(flatten_list(element))
        else:
            result_list.append(element)
    return result_list

def word_frequencies(text: str) -> dict:
    words = re.findall(r'\w+', text.lower())
    return Counter(words)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True
