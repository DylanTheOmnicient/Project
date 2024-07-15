class Vigenere:
    def encrypt(message, key_users):
        key_real = [ord(i) for i in key_users]
        answer = ''
        for i in range(len(message)):
            shift = key_real[i % len(key_real)]
            answer += chr((ord(message[i]) + shift) % 1200)  # Russian lang max
        return answer

    def decrypt(message, key_users):
        key_real = [ord(i) for i in key_users]
        answer = ''
        for i in range(len(message)):
            shift = key_real[i % len(key_real)]
            answer += chr((ord(message[i]) - shift) % 1200)  # Russian lang max
        return answer
