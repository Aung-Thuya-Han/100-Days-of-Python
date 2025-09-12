print(r'''_________                                      _________ .__       .__                  
\_   ___ \_____    ____   ___________ _______  \_   ___ \|__|_____ |  |__   ___________ 
/    \  \/\__  \ _/ __ \ /  ___/\__  \\_  __ \ /    \  \/|  \____ \|  |  \_/ __ \_  __ \
\     \____/ __ \\  ___/ \___ \  / __ \|  | \/ \     \___|  |  |_> >   Y  \  ___/|  | \/
 \______  (____  /\___  >____  >(____  /__|     \______  /__|   __/|___|  /\___  >__|   
        \/     \/     \/     \/      \/                \/   |__|        \/     \/       ''')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encoded_word = []
decoded_word = []

def encoding(word, step):
    for letter in word:
        shifting_word = alphabet.index(letter)
        shifting_word += step
        if len(alphabet) <= shifting_word:
            shifting_word -= len(alphabet)
        encoded_word.append(alphabet[shifting_word])

    print("".join(encoded_word))

def decoding(word, step):
    for letter in word:
        shifting_word = alphabet.index(letter)
        shifting_word -= step
        if len(alphabet) <= shifting_word:
            shifting_word += len(alphabet)
        decoded_word.append(alphabet[shifting_word])

    print("".join(decoded_word))

end_game = False
while not end_game:
    user_entry = input("Type A to encode, B to decode, Q to quit: ").upper()
    if user_entry == "A":
        encode_word = input("Enter the word to encode: ")
        encode_step = int(input("Enter the step to encode: "))

        encoding(encode_word, encode_step)
        encoded_word.clear()

    elif user_entry == "B":
        decode_word = input("Enter the word to decode: ")
        decode_step = int(input("Enter the step to decode: "))

        decoding(decode_word, decode_step)
        decoded_word.clear()

    else:
        print("Bye!")
        end_game = True






