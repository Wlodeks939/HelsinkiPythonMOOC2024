# Write your solution here

def anagrams(text1,text2):
    
    if sorted(text1) == sorted(text2):
        return True
    else:
        return False
    

if __name__ == "__main__":
    anagrams("tame", "meta")
