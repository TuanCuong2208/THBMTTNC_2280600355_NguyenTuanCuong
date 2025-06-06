import ecdsa, os

if not os.path.exists('cipher/cc/keys'):
    os.makedirs('cipher/cc/keys')

class ECCipher:
    def __init__(self):
        pass

    def generate_keys(self):
        # Tạo khóa riêng và khóa công khai
        sk = ecdsa.SigningKey.generate()
        vk = sk.get_verifying_key()
        # Lưu khóa riêng và khóa công khai
        with open('cipher/cc/keys/private.pem', 'wb') as p:
            p.write(sk.to_pem())
        with open('cipher/cc/keys/public.pem', 'wb') as p:
            p.write(vk.to_pem())
        return sk, vk

    def load_keys(self):
        with open('cipher/cc/keys/private.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())
        with open('cipher/cc/keys/public.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())
        return sk, vk

    def sign(self, message, key):
        # Mã hóa tin nhắn bằng khóa riêng
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key):
        _, vk = self.load_keys()
        try:
            # Xác minh tin nhắn bằng khóa công khai
            return vk.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False