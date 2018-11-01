from Crypto.PublicKey import RSA 
    
def generate_RSA(bits=2048):
    '''
    Generate an RSA keypair with an exponent of 65537 in PEM format
    param: bits The key length in bits
    Return private key and public key
    '''
    new_key = RSA.generate(bits, e=65537) 
    public_key = new_key.publickey().exportKey("PEM") 
    private_key = new_key.exportKey("PEM") 
    return private_key, public_key

bits = int(input("Enter bits for RSA key generation (powers of 2): "))

private_key, public_key = generate_RSA(bits)

privateWrite = open('private_key.pem','wb')
publicWrite = open('public_key.pem','wb')
privateWrite.write(private_key)
publicWrite.write(public_key)
