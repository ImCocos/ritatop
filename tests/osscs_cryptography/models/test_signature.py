import unittest

from osscs_cryptography.models import Signature


class TestSignature(unittest.TestCase):
    def test_dunder_str(self) -> None:
        signature = Signature(b'\n\n\n', b'', b'')
        self.assertEqual('Signature()', str(signature))

    def test_load_data(self) -> None:
        public_key = b'public_key'
        sign = b'sign'
        sign_data = b'sign_data'
        signature = Signature(public_key, sign, sign_data)
        self.assertEqual(public_key, signature.public_key)
        self.assertEqual(sign, signature.signature)
        self.assertEqual(sign_data, signature.signature_data)
    
    def test_small_public_key_error(self) -> None:
        signature = Signature(b'', b'', b'')
        self.assertRaises(IndexError, signature.__str__)
