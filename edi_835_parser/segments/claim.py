from edi_835_parser.elements.identifier import Identifier
from edi_835_parser.elements.claim_status import ClaimStatus
from edi_835_parser.elements.dollars import Dollars
from edi_835_parser.segments.utilities import split_segment, get_element


class Claim:
    identification = 'CLP'

    identifier = Identifier()
    status = ClaimStatus()
    charge_amount = Dollars()
    paid_amount = Dollars()

    def __init__(self, segment: str):
        self.segment = segment
        segment = split_segment(segment)

        self.identifier = segment[0]
        self.marker = segment[1]
        self.status = segment[2]
        self.charge_amount = segment[3]
        self.paid_amount = segment[4]
        self.revenue_code = get_element(segment, 6)

    def __repr__(self):
        return '\n'.join(str(item) for item in self.__dict__.items())


if __name__ == '__main__':
    pass
