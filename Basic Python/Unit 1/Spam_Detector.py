spam_words = [
    "Free",
    "Winner",
    "Cash",
    "Click here",
    "Congratulations",
    "Earn money",
    "Exclusive deal",
    "Act now",
    "Risk-free",
    "Limited time offer",
    "100% free",
    "Guarantee",
    "No cost",
    "Prize",
    "Urgent",
    "Special promotion",
    "Buy now",
    "Offer expires",
    "Increase sales",
    "Cheap",
    "Get rich",
    "Viagra",
    "Weight loss",
    "Best price",
    "Save big",
    "Unsubscribe",
    "This isn’t a scam",
    "Limited supply",
    "Discount",
    "Act fast",
    "Promise",
    "Credit card",
    "Fast cash",
    "Instant",
    "Once in a lifetime",
    "Order now"
]

msg  = input("Enter the your message for spam detection: ")

spam_count = 0

for word in spam_words:
    if word.lower() in msg.lower():
        spam_count +=1
        print(f"Spam word found: {word}")
    else :
        print(f"Spam word not found: {word}")    

if spam_count == 0:
    print("This message is spam")
else:
    print("This message is not spam")        