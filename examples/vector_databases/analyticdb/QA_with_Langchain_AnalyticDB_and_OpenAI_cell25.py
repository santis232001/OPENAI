random.seed(41)
for question in random.choices(questions, k=5):
    print(">", question)
    print(custom_qa.run(question), end="\n\n")