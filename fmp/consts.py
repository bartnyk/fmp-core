from enum import Enum


class Currency(Enum):
    USD = "USD"  # United States Dollar
    EUR = "EUR"  # Euro
    JPY = "JPY"  # Japanese Yen
    GBP = "GBP"  # British Pound Sterling
    AUD = "AUD"  # Australian Dollar
    CAD = "CAD"  # Canadian Dollar
    CHF = "CHF"  # Swiss Franc
    CNY = "CNY"  # Chinese Yuan
    HKD = "HKD"  # Hong Kong Dollar
    NZD = "NZD"  # New Zealand Dollar
    SEK = "SEK"  # Swedish Krona
    KRW = "KRW"  # South Korean Won
    SGD = "SGD"  # Singapore Dollar
    NOK = "NOK"  # Norwegian Krone
    MXN = "MXN"  # Mexican Peso
    INR = "INR"  # Indian Rupee
    RUB = "RUB"  # Russian Ruble
    ZAR = "ZAR"  # South African Rand
    TRY = "TRY"  # Turkish Lira
    BRL = "BRL"  # Brazilian Real
    PLN = "PLN"  # Polish Zloty


class Period(Enum):
    ONE_DAY = "1d"  # 1 day
    FIVE_DAYS = "5d"  # 5 days
    ONE_MONTH = "1mo"  # 1 month
    THREE_MONTHS = "3mo"  # 3 months
    SIX_MONTHS = "6mo"  # 6 months
    ONE_YEAR = "1y"  # 1 year
    TWO_YEARS = "2y"  # 2 years
    FIVE_YEARS = "5y"  # 5 years
    TEN_YEARS = "10y"  # 10 years
    YEAR_TO_DATE = "ytd"  # Year to date
    MAX = "max"  # Maximum available period


class Interval(Enum):
    ONE_MINUTE = "1m"  # 1 minute
    TWO_MINUTES = "2m"  # 2 minutes
    FIVE_MINUTES = "5m"  # 5 minutes
    FIFTEEN_MINUTES = "15m"  # 15 minutes
    THIRTY_MINUTES = "30m"  # 30 minutes
    SIXTY_MINUTES = "60m"  # 60 minutes
    NINETY_MINUTES = "90m"  # 90 minutes
    ONE_DAY = "1d"  # 1 day
    FIVE_DAYS = "5d"  # 5 days
    ONE_WEEK = "1wk"  # 1 week
    ONE_MONTH = "1mo"  # 1 month


class Country(Enum):
    """Country subject enumeration class."""

    USA = "United States"
    EU = "Euro Area"
    Japan = "Japan"
    UK = "United Kingdom"
    Australia = "Australia"
    Canada = "Canada"
    Switzerland = "Switzerland"
    China = "China"
    Mexico = "Mexico"
    India = "India"
    Russia = "Russia"
    Turkey = "Turkey"
    Poland = "Poland"

    @property
    def _currencies(self) -> dict:
        return {
            self.USA: "USD",
            self.EU: "EUR",
            self.Japan: "JPY",
            self.UK: "GBP",
            self.Australia: "AUD",
            self.Canada: "CAD",
            self.Switzerland: "CHF",
            self.China: "CNY",
            self.Mexico: "MXN",
            self.India: "INR",
            self.Russia: "RUB",
            self.Turkey: "TRY",
            self.Poland: "PLN",
        }

    @property
    def currency(self) -> str:
        """
        Get the currency of the country.

        Returns
        -------
        str
            Currency code.

        """
        return self._currencies[self]

    @classmethod
    def get_subject_names(cls) -> list[str]:
        """Get the list of country subject names."""
        return [subject.value for subject in cls]


class ForexUpdateType(Enum):
    """Forex update type enumeration class."""

    HISTORICAL = "historical"
    LATEST = "latest"
