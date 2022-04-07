wholeclass ={'John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'}
eng_pass = {'John','Mary','Fiona','Claire','Ben','Bill'}
math_pass = {'Mary','Fiona','Claire','Eva','Ben'} 
print("英文與數學都及格",math_pass&eng_pass)
print("數學不及格",wholeclass-math_pass)
print("英文及格且數學不及格",eng_pass-math_pass)