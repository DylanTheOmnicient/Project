class Caesar:
    def encrypt(message, key_users):
        key_real = int(key_users) % 1200
        answer = ''
        for i in range(len(message)):
            answer += chr((ord(message[i]) + key_real))
        return answer

    def decrypt(message, key_users):
        key_real = int(key_users) % 1200
        answer = ''
        for i in range(len(message)):
            answer += chr((ord(message[i]) - key_real))
        return answer