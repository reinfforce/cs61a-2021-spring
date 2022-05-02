test = {
  'name': 'Problem 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ps = ['short', 'really long', 'tiny']
          >>> s = lambda p: len(p) <= 5
          >>> choose(ps, s, 0) # remember to put quotes ('') around strings!
          'short'
          >>> choose(ps, s, 1)
          'tiny'
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['hi', 'how are you', 'fine']
          >>> s = lambda p: len(p) <= 4
          >>> choose(ps, s, 0)
          'hi'
          >>> choose(ps, s, 1)
          'fine'
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['VQwSwNX']
          >>> s = lambda p: p == 'VQwSwNX'
          >>> choose(ps, s, 0)
          'VQwSwNX'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['d', '6VXy', '9UtlGF3JvN', 'C']
          >>> s = lambda p: p == '6VXy' or p == '9UtlGF3JvN' or p == 'd'
          >>> choose(ps, s, 0)
          'd'
          >>> choose(ps, s, 1)
          '6VXy'
          >>> choose(ps, s, 2)
          '9UtlGF3JvN'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['nmLjTBQ']
          >>> s = lambda p: p == 'nmLjTBQ'
          >>> choose(ps, s, 0)
          'nmLjTBQ'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['LQa7i6tx', '7VNVwiz6', 'FiSMcoBy', 'CbkzHZd8Q', 'wTeIcJF', 'c5', '7qIhVzA']
          >>> s = lambda p: p == '7qIhVzA' or p == 'CbkzHZd8Q' or p == 'c5' or p == 'wTeIcJF'
          >>> choose(ps, s, 0)
          'CbkzHZd8Q'
          >>> choose(ps, s, 1)
          'wTeIcJF'
          >>> choose(ps, s, 2)
          'c5'
          >>> choose(ps, s, 3)
          '7qIhVzA'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['YSw2G9VmQ9', 'ER', 'r7ey5O', 'XO3sj', '2MWemTjKV1', 'ZZIaR', 'TIv0ZHG']
          >>> s = lambda p: p == '2MWemTjKV1'
          >>> choose(ps, s, 0)
          '2MWemTjKV1'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['0lQzW0tyg', 'yvW708v']
          >>> s = lambda p: p == 'yvW708v'
          >>> choose(ps, s, 0)
          'yvW708v'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['auPQIQ7', 'tk7FMoy', 'vNDPPf3d', '2LtT', 'ynsLz', 'frmxE', 'L', 'NKv']
          >>> s = lambda p: p == 'NKv' or p == 'tk7FMoy'
          >>> choose(ps, s, 0)
          'tk7FMoy'
          >>> choose(ps, s, 1)
          'NKv'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['Y', 'ENbBM', 'at4eksVN1', 'o8VT', 'x1a']
          >>> s = lambda p: p == 'ENbBM'
          >>> choose(ps, s, 0)
          'ENbBM'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['l0sZzF']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['RfD92AMft', '1sYnFXT7x', '4G6oqY', 'I8hl', 'I01gb', '1cfGgts', '2tmdpqV6lK', 'WSZ080', '2Zx']
          >>> s = lambda p: p == '1cfGgts' or p == '4G6oqY' or p == 'RfD92AMft' or p == 'WSZ080'
          >>> choose(ps, s, 0)
          'RfD92AMft'
          >>> choose(ps, s, 1)
          '4G6oqY'
          >>> choose(ps, s, 2)
          '1cfGgts'
          >>> choose(ps, s, 3)
          'WSZ080'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['A', 'csq8G', 'YD2HwwOl6', 'N967LBA', 'eoLalNDIm8', '0', 'meY', 'oNxuI8MIY']
          >>> s = lambda p: p == '0' or p == 'N967LBA' or p == 'YD2HwwOl6' or p == 'eoLalNDIm8' or p == 'meY'
          >>> choose(ps, s, 0)
          'YD2HwwOl6'
          >>> choose(ps, s, 1)
          'N967LBA'
          >>> choose(ps, s, 2)
          'eoLalNDIm8'
          >>> choose(ps, s, 3)
          '0'
          >>> choose(ps, s, 4)
          'meY'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['gPfGb2k', 'SFXa56cid5']
          >>> s = lambda p: p == 'SFXa56cid5' or p == 'gPfGb2k'
          >>> choose(ps, s, 0)
          'gPfGb2k'
          >>> choose(ps, s, 1)
          'SFXa56cid5'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['CD', 'h', 'E7']
          >>> s = lambda p: p == 'CD' or p == 'E7'
          >>> choose(ps, s, 0)
          'CD'
          >>> choose(ps, s, 1)
          'E7'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['RfLCTEoQP', 'j', 'KpOY0rO']
          >>> s = lambda p: p == 'RfLCTEoQP'
          >>> choose(ps, s, 0)
          'RfLCTEoQP'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['EdTSBXJusc', 'alRMq', 'op', 'kLZC', 'IpbS9MJ', 'zJLSk8yBg', 'IoT']
          >>> s = lambda p: p == 'IoT' or p == 'IpbS9MJ' or p == 'kLZC' or p == 'zJLSk8yBg'
          >>> choose(ps, s, 0)
          'kLZC'
          >>> choose(ps, s, 1)
          'IpbS9MJ'
          >>> choose(ps, s, 2)
          'zJLSk8yBg'
          >>> choose(ps, s, 3)
          'IoT'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['304lsOWM', '0kx7n']
          >>> s = lambda p: p == '304lsOWM'
          >>> choose(ps, s, 0)
          '304lsOWM'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['GSr', 'H', 'kdps', 'X', 'EFMVi']
          >>> s = lambda p: p == 'EFMVi' or p == 'GSr' or p == 'H' or p == 'X' or p == 'kdps'
          >>> choose(ps, s, 0)
          'GSr'
          >>> choose(ps, s, 1)
          'H'
          >>> choose(ps, s, 2)
          'kdps'
          >>> choose(ps, s, 3)
          'X'
          >>> choose(ps, s, 4)
          'EFMVi'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['93qZ2FApAL', 'lDq', 'Gf', 'JzE', 'z3ZL9ig0', '8AV7vJabk', 'YI6YCcep2B', 'h']
          >>> s = lambda p: p == '8AV7vJabk' or p == '93qZ2FApAL' or p == 'JzE' or p == 'lDq' or p == 'z3ZL9ig0'
          >>> choose(ps, s, 0)
          '93qZ2FApAL'
          >>> choose(ps, s, 1)
          'lDq'
          >>> choose(ps, s, 2)
          'JzE'
          >>> choose(ps, s, 3)
          'z3ZL9ig0'
          >>> choose(ps, s, 4)
          '8AV7vJabk'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['Hc8ZUR', 'lTYGK8fqL', 'k4s3M4qbGv', '0I2', '2x', 'H', 'd2WgDNGyM', 'tZm', 'B2KlNoOK2']
          >>> s = lambda p: p == '2x' or p == 'd2WgDNGyM' or p == 'lTYGK8fqL'
          >>> choose(ps, s, 0)
          'lTYGK8fqL'
          >>> choose(ps, s, 1)
          '2x'
          >>> choose(ps, s, 2)
          'd2WgDNGyM'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['X', 'DY3sRp']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['Ldanr2', '7eCQ', 'uRSJ41vut', 'rgLg', '1', 'HV2Zd9', 'Mb', 'wmk3kbCen']
          >>> s = lambda p: p == 'HV2Zd9' or p == 'Ldanr2' or p == 'wmk3kbCen'
          >>> choose(ps, s, 0)
          'Ldanr2'
          >>> choose(ps, s, 1)
          'HV2Zd9'
          >>> choose(ps, s, 2)
          'wmk3kbCen'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['F', 'MRL', 'H59IjPk']
          >>> s = lambda p: p == 'F'
          >>> choose(ps, s, 0)
          'F'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['mQU9baph', 'ZZYcg3z', 'ywN6dz', 'J39Fd49DZV', 'js', 'MLC']
          >>> s = lambda p: p == 'MLC' or p == 'ywN6dz'
          >>> choose(ps, s, 0)
          'ywN6dz'
          >>> choose(ps, s, 1)
          'MLC'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['PA', 'k8DawMrmv']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['z57ZNLrLs', 'VRaYb1tYo', 'AQ', 'K2ZUMUeb', '16', '0rhAwFK', 'G5WDJkhg', 'SFFRBWZOY']
          >>> s = lambda p: p == '0rhAwFK' or p == 'K2ZUMUeb' or p == 'VRaYb1tYo' or p == 'z57ZNLrLs'
          >>> choose(ps, s, 0)
          'z57ZNLrLs'
          >>> choose(ps, s, 1)
          'VRaYb1tYo'
          >>> choose(ps, s, 2)
          'K2ZUMUeb'
          >>> choose(ps, s, 3)
          '0rhAwFK'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['F', 'hyZN', 'ZY', 'vnp3634n', 'FLXmF7Lct6', 'ew', 'EvEi9ENwsx', 'w3YnNbSmn', 'tGsGhvAsH8']
          >>> s = lambda p: p == 'EvEi9ENwsx' or p == 'F' or p == 'ZY' or p == 'tGsGhvAsH8'
          >>> choose(ps, s, 0)
          'F'
          >>> choose(ps, s, 1)
          'ZY'
          >>> choose(ps, s, 2)
          'EvEi9ENwsx'
          >>> choose(ps, s, 3)
          'tGsGhvAsH8'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['uND35F', 'c25CIccuvf', 'Q2hf9', 'h', '76']
          >>> s = lambda p: p == '76' or p == 'Q2hf9' or p == 'h' or p == 'uND35F'
          >>> choose(ps, s, 0)
          'uND35F'
          >>> choose(ps, s, 1)
          'Q2hf9'
          >>> choose(ps, s, 2)
          'h'
          >>> choose(ps, s, 3)
          '76'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['X', 'DlPnvunj7T', 'eYRTlaACA', 'd', 'zsns3L', '7Iqa4', 'uCP1go']
          >>> s = lambda p: p == '7Iqa4' or p == 'DlPnvunj7T' or p == 'X' or p == 'd' or p == 'eYRTlaACA'
          >>> choose(ps, s, 0)
          'X'
          >>> choose(ps, s, 1)
          'DlPnvunj7T'
          >>> choose(ps, s, 2)
          'eYRTlaACA'
          >>> choose(ps, s, 3)
          'd'
          >>> choose(ps, s, 4)
          '7Iqa4'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['0pLcv1']
          >>> s = lambda p: p == '0pLcv1'
          >>> choose(ps, s, 0)
          '0pLcv1'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['NILkkPinUi', 't0', 'v', 'R4U', 'u4o', 'wr9XAN', 'UxSdAGf6j']
          >>> s = lambda p: p == 'R4U' or p == 't0'
          >>> choose(ps, s, 0)
          't0'
          >>> choose(ps, s, 1)
          'R4U'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['Gp', 'iZg', 'IqbFcokMP', 't4RSwwh', 'Ctxpyk3', '5CGYzYN1p9', 'JKg11tt', 'D']
          >>> s = lambda p: p == 'Gp' or p == 'IqbFcokMP' or p == 'iZg'
          >>> choose(ps, s, 0)
          'Gp'
          >>> choose(ps, s, 1)
          'iZg'
          >>> choose(ps, s, 2)
          'IqbFcokMP'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['5', 'gl2lj5soWr', 'e4UQ2d', 'o2T', 'tIUGQKT']
          >>> s = lambda p: p == '5' or p == 'e4UQ2d' or p == 'o2T' or p == 'tIUGQKT'
          >>> choose(ps, s, 0)
          '5'
          >>> choose(ps, s, 1)
          'e4UQ2d'
          >>> choose(ps, s, 2)
          'o2T'
          >>> choose(ps, s, 3)
          'tIUGQKT'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['U', 'sR3WXvxV0h', 'pjGtb4EZ1', 'MqO', 'i0R']
          >>> s = lambda p: p == 'U' or p == 'pjGtb4EZ1' or p == 'sR3WXvxV0h'
          >>> choose(ps, s, 0)
          'U'
          >>> choose(ps, s, 1)
          'sR3WXvxV0h'
          >>> choose(ps, s, 2)
          'pjGtb4EZ1'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['1', '1gN1', 'm', 'wtM0', 'EXqazAV', '82Jrsbx']
          >>> s = lambda p: p == '1' or p == 'm' or p == 'wtM0'
          >>> choose(ps, s, 0)
          '1'
          >>> choose(ps, s, 1)
          'm'
          >>> choose(ps, s, 2)
          'wtM0'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['L1SchAt4fb', 'PZxrWEu', 'Z']
          >>> s = lambda p: p == 'L1SchAt4fb' or p == 'Z'
          >>> choose(ps, s, 0)
          'L1SchAt4fb'
          >>> choose(ps, s, 1)
          'Z'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['ipYmZQQ', 'WlG', 'PGT9UN', '0k0JqROEtL', 'InWB86Ezx', 'pr']
          >>> s = lambda p: p == '0k0JqROEtL' or p == 'pr'
          >>> choose(ps, s, 0)
          '0k0JqROEtL'
          >>> choose(ps, s, 1)
          'pr'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['uilC', '5C', 'du2lbz', 'C0']
          >>> s = lambda p: p == '5C' or p == 'du2lbz' or p == 'uilC'
          >>> choose(ps, s, 0)
          'uilC'
          >>> choose(ps, s, 1)
          '5C'
          >>> choose(ps, s, 2)
          'du2lbz'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['iQ7fUEGX', 'yYpvrxFw', 'XD', 'SZuNFuOl9G', 'Y', 'D9GOm', 'mhEzPwaQ', 'OK6V']
          >>> s = lambda p: p == 'D9GOm' or p == 'SZuNFuOl9G' or p == 'XD' or p == 'iQ7fUEGX'
          >>> choose(ps, s, 0)
          'iQ7fUEGX'
          >>> choose(ps, s, 1)
          'XD'
          >>> choose(ps, s, 2)
          'SZuNFuOl9G'
          >>> choose(ps, s, 3)
          'D9GOm'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['mKXoHy', 'uwN9gNbHUs', 'B', 'oiQsIfR', 'wy2', 'ydYhiQAYge', 'tsZiGcHBky']
          >>> s = lambda p: p == 'B' or p == 'mKXoHy' or p == 'uwN9gNbHUs'
          >>> choose(ps, s, 0)
          'mKXoHy'
          >>> choose(ps, s, 1)
          'uwN9gNbHUs'
          >>> choose(ps, s, 2)
          'B'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['P3bKdUdm3', 'm', 'Mf0', '4']
          >>> s = lambda p: p == 'Mf0' or p == 'P3bKdUdm3'
          >>> choose(ps, s, 0)
          'P3bKdUdm3'
          >>> choose(ps, s, 1)
          'Mf0'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['s02mysRaP']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['xIg', 'B8CtQlMiZ', 'es', 'DQUyran1G3', 'uV0H45P', 'zq', 'ZR3FZxesMP', 'H3YQpNd8', '6gY']
          >>> s = lambda p: p == '6gY' or p == 'H3YQpNd8' or p == 'ZR3FZxesMP' or p == 'xIg' or p == 'zq'
          >>> choose(ps, s, 0)
          'xIg'
          >>> choose(ps, s, 1)
          'zq'
          >>> choose(ps, s, 2)
          'ZR3FZxesMP'
          >>> choose(ps, s, 3)
          'H3YQpNd8'
          >>> choose(ps, s, 4)
          '6gY'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['nOOofieJ9', 'adYNFKzY', 'oq', 'm2bMd96oQk']
          >>> s = lambda p: p == 'adYNFKzY' or p == 'm2bMd96oQk' or p == 'oq'
          >>> choose(ps, s, 0)
          'adYNFKzY'
          >>> choose(ps, s, 1)
          'oq'
          >>> choose(ps, s, 2)
          'm2bMd96oQk'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['EWv', 'gGgVsIrdaw']
          >>> s = lambda p: p == 'EWv'
          >>> choose(ps, s, 0)
          'EWv'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['Ow3a998p', 'enyrA', 'lRY672', 'wCB', 'vX2kPf', '1chq', 'ixgdI']
          >>> s = lambda p: p == 'Ow3a998p' or p == 'vX2kPf' or p == 'wCB'
          >>> choose(ps, s, 0)
          'Ow3a998p'
          >>> choose(ps, s, 1)
          'wCB'
          >>> choose(ps, s, 2)
          'vX2kPf'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['Rch', 'CPOMxX', 'UU0LYC1O', 'xv2pCJOXo', 'zcZ280', 'y7WHG4y', 'L']
          >>> s = lambda p: p == 'Rch' or p == 'zcZ280'
          >>> choose(ps, s, 0)
          'Rch'
          >>> choose(ps, s, 1)
          'zcZ280'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['zDmdJf4', 'fUBVpey', 'HqlP2', 'vZN', 'nU51ij', 'v7f', 'YZ7xFI']
          >>> s = lambda p: p == 'HqlP2' or p == 'fUBVpey' or p == 'nU51ij' or p == 'zDmdJf4'
          >>> choose(ps, s, 0)
          'zDmdJf4'
          >>> choose(ps, s, 1)
          'fUBVpey'
          >>> choose(ps, s, 2)
          'HqlP2'
          >>> choose(ps, s, 3)
          'nU51ij'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['f4A']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['Xrzwzt', 'v', 'KX', 'H3d2xZ', '4v']
          >>> s = lambda p: p == '4v' or p == 'H3d2xZ' or p == 'KX' or p == 'Xrzwzt'
          >>> choose(ps, s, 0)
          'Xrzwzt'
          >>> choose(ps, s, 1)
          'KX'
          >>> choose(ps, s, 2)
          'H3d2xZ'
          >>> choose(ps, s, 3)
          '4v'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['dDwAGMgl', 'l4X56Bpz', 'h7pz1nX', 'jRl', 'ND', 'g', 'Q2A', 'vnrI', '2mxw']
          >>> s = lambda p: p == '2mxw' or p == 'ND' or p == 'g'
          >>> choose(ps, s, 0)
          'ND'
          >>> choose(ps, s, 1)
          'g'
          >>> choose(ps, s, 2)
          '2mxw'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['TSYkVXX8J', 'frYDl', 'YA46ttJC', 'l', 'FKtASZR', 'BDzdcFxX', 'ogN7N2k15y', 'dYj8sYDhxC', 'VgknQ']
          >>> s = lambda p: p == 'VgknQ' or p == 'YA46ttJC' or p == 'l'
          >>> choose(ps, s, 0)
          'YA46ttJC'
          >>> choose(ps, s, 1)
          'l'
          >>> choose(ps, s, 2)
          'VgknQ'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['qN9RUqUGE', 'k46wF6wOD', 'OeXJBkF', 'w', 'Mx']
          >>> s = lambda p: p == 'OeXJBkF' or p == 'k46wF6wOD' or p == 'w'
          >>> choose(ps, s, 0)
          'k46wF6wOD'
          >>> choose(ps, s, 1)
          'OeXJBkF'
          >>> choose(ps, s, 2)
          'w'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['YzL0HHUD7k']
          >>> s = lambda p: p == 'YzL0HHUD7k'
          >>> choose(ps, s, 0)
          'YzL0HHUD7k'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['bAS4fmgP', 'Nn', 'FJjnXVE9Ul', 'OT5yBSF', 'GO32eXGldm', '8', 'hdQYZK']
          >>> s = lambda p: p == '8' or p == 'FJjnXVE9Ul' or p == 'GO32eXGldm'
          >>> choose(ps, s, 0)
          'FJjnXVE9Ul'
          >>> choose(ps, s, 1)
          'GO32eXGldm'
          >>> choose(ps, s, 2)
          '8'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['o83']
          >>> s = lambda p: p == 'o83'
          >>> choose(ps, s, 0)
          'o83'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['mJU', 'bs0DSA02C']
          >>> s = lambda p: p == 'bs0DSA02C'
          >>> choose(ps, s, 0)
          'bs0DSA02C'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['8pds2kPGPz', 'sCQRiD', 'yLf6i0B3Q']
          >>> s = lambda p: p == '8pds2kPGPz'
          >>> choose(ps, s, 0)
          '8pds2kPGPz'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['NrH', 'NGabhb', 'w33y19SdHp', 'lB1Lz', 'fK', '0eewNgUHY', 'z7T0j5', '0MlPnj', 'ji5Nw']
          >>> s = lambda p: p == '0MlPnj' or p == '0eewNgUHY' or p == 'NGabhb' or p == 'NrH' or p == 'fK' or p == 'ji5Nw' or p == 'z7T0j5'
          >>> choose(ps, s, 0)
          'NrH'
          >>> choose(ps, s, 1)
          'NGabhb'
          >>> choose(ps, s, 2)
          'fK'
          >>> choose(ps, s, 3)
          '0eewNgUHY'
          >>> choose(ps, s, 4)
          'z7T0j5'
          >>> choose(ps, s, 5)
          '0MlPnj'
          >>> choose(ps, s, 6)
          'ji5Nw'
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['Ha', 'Xifelge', 'xoI', 'w73OM', 'iYNWXJ59v']
          >>> s = lambda p: p == 'Xifelge' or p == 'iYNWXJ59v' or p == 'xoI'
          >>> choose(ps, s, 0)
          'Xifelge'
          >>> choose(ps, s, 1)
          'xoI'
          >>> choose(ps, s, 2)
          'iYNWXJ59v'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['kDfhLe4La0']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['kX1sidw3UT', 'ZMI1uuiAae', 'kk9WcBKN', '3CqQNllBRZ', 'nhx8BfZH3P']
          >>> s = lambda p: p == 'ZMI1uuiAae' or p == 'kk9WcBKN' or p == 'nhx8BfZH3P'
          >>> choose(ps, s, 0)
          'ZMI1uuiAae'
          >>> choose(ps, s, 1)
          'kk9WcBKN'
          >>> choose(ps, s, 2)
          'nhx8BfZH3P'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['qzxR', 'DhdP0zHm', '2JHw', 'BeDWISwn']
          >>> s = lambda p: p == 'BeDWISwn'
          >>> choose(ps, s, 0)
          'BeDWISwn'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['2ZD2', 'Ujvf7Z']
          >>> s = lambda p: p == '2ZD2'
          >>> choose(ps, s, 0)
          '2ZD2'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['sqRXmfefZu', 'VG', 'Ugij', 'MDXm', '4dJa', 'ppk1Oz', 'Q7fJgP9', 'IYy', 'F8Jyws']
          >>> s = lambda p: p == '4dJa' or p == 'F8Jyws' or p == 'IYy' or p == 'MDXm' or p == 'VG'
          >>> choose(ps, s, 0)
          'VG'
          >>> choose(ps, s, 1)
          'MDXm'
          >>> choose(ps, s, 2)
          '4dJa'
          >>> choose(ps, s, 3)
          'IYy'
          >>> choose(ps, s, 4)
          'F8Jyws'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['uenSyKB6', 'd5Z7i', 'hDgbK6']
          >>> s = lambda p: p == 'hDgbK6'
          >>> choose(ps, s, 0)
          'hDgbK6'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['YAaF', 'LtejXQR3I', 'S348mz', 'QY']
          >>> s = lambda p: p == 'QY' or p == 'S348mz'
          >>> choose(ps, s, 0)
          'S348mz'
          >>> choose(ps, s, 1)
          'QY'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['AiRBkNK', 'l', '2IK', 'Xk', 'X', 'jckGefD', 'n5nSrsZWH', 'W5TO4oty2']
          >>> s = lambda p: p == 'AiRBkNK' or p == 'X' or p == 'Xk' or p == 'jckGefD' or p == 'l' or p == 'n5nSrsZWH'
          >>> choose(ps, s, 0)
          'AiRBkNK'
          >>> choose(ps, s, 1)
          'l'
          >>> choose(ps, s, 2)
          'Xk'
          >>> choose(ps, s, 3)
          'X'
          >>> choose(ps, s, 4)
          'jckGefD'
          >>> choose(ps, s, 5)
          'n5nSrsZWH'
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['u2z7Y03iJc', 'RuNhLK']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['m6uQ24YvD']
          >>> s = lambda p: p == 'm6uQ24YvD'
          >>> choose(ps, s, 0)
          'm6uQ24YvD'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['B7Tx', '0yk1qfrx', '3aGm', 'TGHqcxtoTW', '13O6gwPzxF', 'TJ2VQS']
          >>> s = lambda p: p == '0yk1qfrx'
          >>> choose(ps, s, 0)
          '0yk1qfrx'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['0lkP']
          >>> s = lambda p: p == '0lkP'
          >>> choose(ps, s, 0)
          '0lkP'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['VykeNT', 'dpbP1sL', 'Jn5Ifn', 'yq']
          >>> s = lambda p: p == 'Jn5Ifn' or p == 'VykeNT' or p == 'yq'
          >>> choose(ps, s, 0)
          'VykeNT'
          >>> choose(ps, s, 1)
          'Jn5Ifn'
          >>> choose(ps, s, 2)
          'yq'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['BdydSkvf', 'uL6Yj', 'PixYkaj', 'tEc', 'DMDnhULpwQ', 'SMG0aYMH9q']
          >>> s = lambda p: p == 'BdydSkvf' or p == 'DMDnhULpwQ'
          >>> choose(ps, s, 0)
          'BdydSkvf'
          >>> choose(ps, s, 1)
          'DMDnhULpwQ'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['NgfFbsH', 'PesgKW6q', 'Iy6d', '6', 'p7lmmO63G', 'jeYUS0wUf', 'I']
          >>> s = lambda p: p == 'I' or p == 'p7lmmO63G'
          >>> choose(ps, s, 0)
          'p7lmmO63G'
          >>> choose(ps, s, 1)
          'I'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['sPTbNQRAhh', 'IVEczM', 'fA9', 'A0AY9T', '7LJbrLU', 'Sjq', 'Z8PpCHs']
          >>> s = lambda p: p == '7LJbrLU' or p == 'fA9'
          >>> choose(ps, s, 0)
          'fA9'
          >>> choose(ps, s, 1)
          '7LJbrLU'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['rUEGEUqg', 'oHHWXQ0', 'x', 'a1', 'qxt', 'PjB7RBX', 't5nL', 'qDpQGg']
          >>> s = lambda p: p == 'qDpQGg' or p == 'rUEGEUqg' or p == 't5nL' or p == 'x'
          >>> choose(ps, s, 0)
          'rUEGEUqg'
          >>> choose(ps, s, 1)
          'x'
          >>> choose(ps, s, 2)
          't5nL'
          >>> choose(ps, s, 3)
          'qDpQGg'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['i0xU89vb', 'fbLYeUU1En', 'sKbLE5N', 'rN', 'MLvZH4fHmU', 'c3BNQKY2', 'ce']
          >>> s = lambda p: p == 'MLvZH4fHmU' or p == 'ce' or p == 'sKbLE5N'
          >>> choose(ps, s, 0)
          'sKbLE5N'
          >>> choose(ps, s, 1)
          'MLvZH4fHmU'
          >>> choose(ps, s, 2)
          'ce'
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['cIr8', 'skx4gl', '1SpUj', 'MYn09BdVIZ', 'Om7eLp7H']
          >>> s = lambda p: p == 'MYn09BdVIZ'
          >>> choose(ps, s, 0)
          'MYn09BdVIZ'
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['GP108P', 'Mll7S8u', 'GffkIsAPzQ', 'hDAuAO', '8Kdsy', 'GySxVZen', 'wI5Tkn4bwx', 'WICmWpO']
          >>> s = lambda p: p == '8Kdsy' or p == 'GffkIsAPzQ' or p == 'Mll7S8u' or p == 'wI5Tkn4bwx'
          >>> choose(ps, s, 0)
          'Mll7S8u'
          >>> choose(ps, s, 1)
          'GffkIsAPzQ'
          >>> choose(ps, s, 2)
          '8Kdsy'
          >>> choose(ps, s, 3)
          'wI5Tkn4bwx'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['wkRz']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['OXAbRon7U9', '4JMu7xz', 'k750O', 'jZrOMXgZt', 'y', '6U5', 'XBIuxFY', 'R3XBpqe']
          >>> s = lambda p: p == '6U5' or p == 'OXAbRon7U9' or p == 'R3XBpqe' or p == 'jZrOMXgZt' or p == 'k750O' or p == 'y'
          >>> choose(ps, s, 0)
          'OXAbRon7U9'
          >>> choose(ps, s, 1)
          'k750O'
          >>> choose(ps, s, 2)
          'jZrOMXgZt'
          >>> choose(ps, s, 3)
          'y'
          >>> choose(ps, s, 4)
          '6U5'
          >>> choose(ps, s, 5)
          'R3XBpqe'
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['faiJn']
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          >>> choose(ps, s, 2)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['IFHBTB', 'eMXHdke', 'aMaIJ', 'koTYt5O', 'Ab', 'CBJUDV', 'pyN', '6N6SK', '1EWs']
          >>> s = lambda p: p == '1EWs' or p == 'Ab' or p == 'CBJUDV' or p == 'IFHBTB'
          >>> choose(ps, s, 0)
          'IFHBTB'
          >>> choose(ps, s, 1)
          'Ab'
          >>> choose(ps, s, 2)
          'CBJUDV'
          >>> choose(ps, s, 3)
          '1EWs'
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          >>> choose(ps, s, 10)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['6', 'wbpawG', 'UiKIi', 'OZcIyYtUoi', 'saYIfJm', 'q', 'M1o6Qa2b']
          >>> s = lambda p: p == '6' or p == 'q'
          >>> choose(ps, s, 0)
          '6'
          >>> choose(ps, s, 1)
          'q'
          >>> choose(ps, s, 2)
          ''
          >>> choose(ps, s, 3)
          ''
          >>> choose(ps, s, 4)
          ''
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = []
          >>> s = lambda p: False
          >>> choose(ps, s, 0)
          ''
          >>> choose(ps, s, 1)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> ps = ['7el', 'Z', 'XrPiLRvY', 'EPIVxh0', 'o6ExRy8l', 'pD4', 'w7cl', '3TVF7bq']
          >>> s = lambda p: p == '3TVF7bq' or p == '7el' or p == 'Z' or p == 'pD4' or p == 'w7cl'
          >>> choose(ps, s, 0)
          '7el'
          >>> choose(ps, s, 1)
          'Z'
          >>> choose(ps, s, 2)
          'pD4'
          >>> choose(ps, s, 3)
          'w7cl'
          >>> choose(ps, s, 4)
          '3TVF7bq'
          >>> choose(ps, s, 5)
          ''
          >>> choose(ps, s, 6)
          ''
          >>> choose(ps, s, 7)
          ''
          >>> choose(ps, s, 8)
          ''
          >>> choose(ps, s, 9)
          ''
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from cats import choose
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
