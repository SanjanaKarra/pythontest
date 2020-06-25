text = "X-DSPAM-Confidence:    0.8475"
t=text.find('0')
e=text[t:t+6]
x=float(e)
print(x)
