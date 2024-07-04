import unittest
from unittest.mock import patch

def transforma(obiect):
    if isinstance(obiect, str):
        return obiect.upper()
    elif isinstance(obiect, (int, float, complex)):
        return obiect ** 2
    else:
        return obiect
    
def proceseaza(lista):
    if not isinstance(lista, list):
        raise TypeError('Parametrul trebuie sa fie lista')
    return [transforma(elem) for elem in lista]


class TestProceseaza(unittest.TestCase):

    @patch('__main__.transforma')
    def test_proceseaza(self, mock_transforma):
        mock_transforma.side_effect = lambda x: f'mocked_{x}'

        lista_test = ['a', 1, 2.0, 'b']

        output_asteptat = ['mocked_a', 'mocked_1', 'mocked_2.0', 'mocked_b']

        rezultat = proceseaza(lista_test)
        self.assertEqual(rezultat, output_asteptat)

        mock_transforma.assert_any_call('a')
        mock_transforma.assert_any_call(1)
        mock_transforma.assert_any_call(2.0)
        mock_transforma.assert_any_call('b')

        self.assertEqual(mock_transforma.call_count, 4)

    def test_proceseaza_fara_lista(self):
        with self.assertRaises(TypeError):
            proceseaza('nu este o lista')

if __name__ == '__main__':
    unittest.main()


    


