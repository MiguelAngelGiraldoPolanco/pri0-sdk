from .be import BEPatterns
from .ch import CHPatterns
from .de import DEPatterns
from .dk import DKPatterns
from .es import ESPatterns
from .fr import FRPatterns
from .gb import GBPatterns
from .ie import IEPatterns
from .nl import NLPatterns
from .pl import PLPatterns
from .pt import PTPatterns
from .se import SEPatterns

country_providers = {
    "be": BEPatterns(),
    "ch": CHPatterns(),
    "de": DEPatterns(),
    "dk": DKPatterns(),
    "es": ESPatterns(),
    "fr": FRPatterns(),
    "gb": GBPatterns(),
    "ie": IEPatterns(),
    "nl": NLPatterns(),
    "pl": PLPatterns(),
    "pt": PTPatterns(),
    "se": SEPatterns(),
}
