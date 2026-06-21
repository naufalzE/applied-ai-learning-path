def count_user_messages(messages):
    user_msg = 0
    for i in messages:
        if i["role"] == "user":
            user_msg+=1
    return user_msg
def count_assistant_msg(messages):
    assistant_msg = 0
    for i in messages:
        if i["role"] == "assistant":
            assistant_msg+=1
    return assistant_msg
def show_user_messages(messages):
    for i in messages:
        if i["role"] == "user":
            print(i["content"])
def show_assistant_messages(messages):
    for i in messages:
        if i["role"] == "assistant":
            print(i["content"])
def get_longest_message(messages):
    panjang_content = 0
    top = ""
    for i in messages:
        if panjang_content < len(i["content"]):
            panjang_content = len(i["content"])
            top = i["content"]
    return top,panjang_content
def count_words(messages):
    total = 0
    for i in messages:
        daftar_kata = i["content"].split()
        total += len(daftar_kata)
    return total
messages = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi"},
    {"role": "user", "content": "How are you?"},
    {"role": "assistant", "content": "I am fine"},
    {"role": "user", "content": "What is Python?"}
]

print("total user msg :",count_user_messages(messages))
print("total assistant msg :",count_assistant_msg(messages))
print("===User Message===")
show_user_messages(messages)
print("===Assistant Message===")
show_assistant_messages(messages)
print("==================")

top,panjang_content = get_longest_message(messages)
print("content  :",top)
print("panjang",panjang_content)


print("total kata   :",count_words(messages))