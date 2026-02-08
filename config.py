"""
HP-Pulse Scraper Configuration
"""

import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# ============================================
# DATABASE
# ============================================
DATABASE_PATH = os.getenv('DATABASE_PATH', 'hp_pulse.db')

# ============================================
# SCRAPING INTERVALS (in hours)
# ============================================
TENDER_INTERVAL = int(os.getenv('TENDER_INTERVAL', '1'))
NEWS_INTERVAL = int(os.getenv('NEWS_INTERVAL', '6'))
DIRECTORY_INTERVAL = int(os.getenv('DIRECTORY_INTERVAL', '24'))

# ============================================
# RATE LIMITING
# ============================================
REQUESTS_PER_SECOND = int(os.getenv('REQUESTS_PER_SECOND', '1'))  # Max 1 request per second per domain
REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', '15'))     # Seconds

# ============================================
# USER AGENT
# ============================================
USER_AGENT = os.getenv('USER_AGENT', 'HP-Pulse-Research-Bot/1.0 (HPCL Direct Sales Research; compliance@hpcl.co.in)')

# ============================================
# KEYWORDS
# ============================================
FUEL_KEYWORDS = [
    'fuel', 'diesel', 'HSD', 'petrol', 'MS', 
    'furnace oil', 'FO', 'LSHS', 'LDO', 'SKO',
    'bitumen', 'hexane', 'solvent', 'lubricant',
    'marine fuel', 'bunker', 'turpentine', 'propylene',
    'jute batch oil', 'JBO', 'mineral turpentine'
]

OPERATIONAL_KEYWORDS = [
    'boiler', 'furnace', 'genset', 'generator',
    'captive power', 'road construction', 'highway',
    'shipping', 'textile', 'jute mill', 'refinery',
    'expansion', 'commissioning', 'new plant',
    'manufacturing', 'facility', 'industrial'
]

TENDER_KEYWORDS = FUEL_KEYWORDS + [
    'tender', 'RFP', 'RFQ', 'quotation', 'procurement',
    'bid', 'contract', 'supply'
]

# ============================================
# SOURCES CONFIGURATION
# ============================================
SOURCES = {
    'tenders': {
        'interval_hours': TENDER_INTERVAL,
        'sources': [
            {
                'name': 'CPP Portal - Fuel Tenders',
                'url': 'https://eprocure.gov.in/eprocure/app',
                'enabled': True,
                'trust_score': 10,
                'description': 'Central Public Procurement Portal'
            },
            {
                'name': 'GEM Portal',
                'url': 'https://gem.gov.in/',
                'enabled': True,
                'trust_score': 10,
                'description': 'Government e-Marketplace'
            }
        ]
    },
    'news': {
        'interval_hours': NEWS_INTERVAL,
        'sources': [
            {
                'name': 'Economic Times - Industry',
                'url': 'https://economictimes.indiatimes.com/industry',
                'rss': 'https://economictimes.indiatimes.com/industry/rssfeeds/13352306.cms',
                'enabled': True,
                'trust_score': 9,
                'description': 'Economic Times Industry News RSS'
            },
            {
                'name': 'Business Standard - Companies',
                'url': 'https://www.business-standard.com/companies',
                'rss': 'https://www.business-standard.com/rss/companies-101.rss',
                'enabled': True,
                'trust_score': 9,
                'description': 'Business Standard Companies RSS'
            },
            {
                'name': 'Hindu Business Line - Industry',
                'url': 'https://www.thehindubusinessline.com/economy/industry/',
                'enabled': True,
                'trust_score': 8,
                'description': 'Hindu Business Line Industry'
            },
            {
                'name': 'PTI News - Business',
                'url': 'https://www.ptinews.com/business',
                'enabled': True,
                'trust_score': 9,
                'description': 'Press Trust of India Business News'
            }
        ]
    },
    'directories': {
        'interval_hours': DIRECTORY_INTERVAL,
        'sources': [
            {
                'name': 'IndiaMART - Chemical Industry',
                'url': 'https://www.indiamart.com/impcat/chemical-industry.html',
                'enabled': True,
                'trust_score': 7,
                'description': 'IndiaMART Chemical Companies Directory'
            },
            {
                'name': 'TradeIndia - Petroleum Products',
                'url': 'https://www.tradeindia.com/petroleum-products/',
                'enabled': False,  # Disabled by default
                'trust_score': 7,
                'description': 'TradeIndia Petroleum Directory'
            }
        ]
    }
}

# ============================================
# HPCL-SPECIFIC CONFIGURATION
# ============================================
HPCL_PRODUCTS = {
    'fuels': ['MS', 'HSD', 'LDO', 'FO', 'LSHS', 'SKO'],
    'specialty': ['Hexane', 'Solvent 1425', 'Mineral Turpentine Oil', 'Jute Batch Oil', 'Propylene'],
    'lubricants': ['HP Milcy', 'HP Racer4', 'HP Enklo', 'HP Lithon'],
    'other': ['Bitumen', 'Marine Bunker Fuel', 'Sulphur']
}

HPCL_REFINERIES = [
    {'name': 'Mumbai Refinery', 'location': 'Mumbai, Maharashtra'},
    {'name': 'Visakhapatnam Refinery', 'location': 'Visakhapatnam, Andhra Pradesh'},
    {'name': 'Bathinda Refinery', 'location': 'Bathinda, Punjab'}
]
