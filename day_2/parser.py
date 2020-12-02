from typing import List


class Password():
    """Password class for holding parsed password data and validation information."""

    def __init__(self, num_high: int,
                 num_low: int,
                 char: str,
                 plaintext: str):

        self.num_high = num_high
        self.num_low = num_low
        self.char = char
        self.plaintext = plaintext
        self.is_valid_part_1 = self._validate_pw_part_1()
        self.is_valid_part_2 = self._validate_pw_part_2()

    def _validate_pw_part_1(self):
        """If char occurrences are within limits, password is considered valid."""
        occurrences = self.plaintext.count(self.char)
        if self.num_low <= occurrences <= self.num_high:
            return True
        return False

    def _validate_pw_part_2(self):
        """If char occurrences are exactly 1, password is concidered valid."""
        chars = self.plaintext[self.num_low-1]+self.plaintext[self.num_high-1]
        if chars.count(self.char) == 1:
            return True
        return False

    def __str__(self):
        return self.plaintext


def read_passwords() -> List[Password]:
    """Read and split passwords."""
    pws = []
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            raw_pw = line[:-1].split(' ')
            lim = raw_pw[0].split('-')
            pws.append(Password(
                int(lim[1]),
                int(lim[0]),
                raw_pw[1][:-1],
                raw_pw[2]),
            )
    return pws


def get_valid_passwords(pws: List[Password]) -> int:
    """Iterate and check validity of all parsed passwords (part 1/2)."""
    valid_part_1_pws = 0
    valid_part_2_pws = 0
    for pw in pws:
        if pw.is_valid_part_1:
            valid_part_1_pws += 1
        if pw.is_valid_part_2:
            valid_part_2_pws += 1
    return (valid_part_1_pws, valid_part_2_pws)


pws = read_passwords()

valid_part_1_pws, valid_part_2_pws = get_valid_passwords(pws)
print(f'Valid part 1 passwords: {valid_part_1_pws}')
print(f'Valid part 2 passwords: {valid_part_2_pws}')
