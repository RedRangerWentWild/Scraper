"""
Tender Scraper for HP-Pulse
Scrapes government tender portals
"""

from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re
from config import TENDER_KEYWORDS
import random

class TenderScraper:
    def __init__(self, db, compliance_checker):
        self.db = db
        self.checker = compliance_checker
        print("✅ Tender scraper initialized")
    
    def is_relevant(self, text):
        """Check if tender is relevant"""
        text_lower = text.lower()
        return any(kw.lower() in text_lower for kw in TENDER_KEYWORDS)
    
    def scrape_cpp_portal(self, source):
        """
        Scrape CPP Portal
        Note: CPP Portal requires JavaScript and authentication
        This uses sample/mock data for demo purposes
        For production, use Selenium + authentication or official API if available
        """
        print(f"\n🏛️  Scraping: {source['name']}")
        print(f"   URL: {source['url']}")
        print("   ⚠️  Note: CPP Portal requires authentication")
        print("   Using representative sample data for demonstration")
        
        # Sample tender data representing typical fuel/chemical tenders
        sample_tenders = [
            {
                'title': 'Supply of High Speed Diesel (HSD) for Power Generation Units',
                'organization': 'Maharashtra State Electricity Distribution Company Limited',
                'value': '₹50,00,000',
                'deadline': (datetime.now() + timedelta(days=15)).strftime('%Y-%m-%d'),
                'location': 'Mumbai, Maharashtra'
            },
            {
                'title': 'Procurement of Bitumen Grade 80/100 for Road Construction',
                'organization': 'National Highways Authority of India (NHAI)',
                'value': '₹2,50,00,000',
                'deadline': (datetime.now() + timedelta(days=8)).strftime('%Y-%m-%d'),
                'location': 'Rajasthan'
            },
            {
                'title': 'Supply of Furnace Oil (FO) for Industrial Boilers',
                'organization': 'Gujarat Industries Power Company Limited',
                'value': '₹1,20,00,000',
                'deadline': (datetime.now() + timedelta(days=20)).strftime('%Y-%m-%d'),
                'location': 'Vadodara, Gujarat'
            },
            {
                'title': 'Light Diesel Oil (LDO) Supply Contract - Annual',
                'organization': 'Indian Railways - Central Railway Zone',
                'value': '₹3,00,00,000',
                'deadline': (datetime.now() + timedelta(days=12)).strftime('%Y-%m-%d'),
                'location': 'Multiple Locations'
            },
            {
                'title': 'Marine Bunker Fuel Supply for Shipping Fleet',
                'organization': 'Shipping Corporation of India',
                'value': '₹5,00,00,000',
                'deadline': (datetime.now() + timedelta(days=18)).strftime('%Y-%m-%d'),
                'location': 'Mumbai, Visakhapatnam'
            }
        ]
        
        # Randomly select 2-4 tenders to simulate scraping
        selected_tenders = random.sample(sample_tenders, k=random.randint(2, 4))
        
        items_found = 0
        for tender in selected_tenders:
            if self.is_relevant(tender['title']):
                # Insert company/organization
                company_id = self.db.insert_company(
                    name=tender['organization'],
                    industry='Government/PSU',
                    location=tender['location']
                )
                
                # Create signal text
                signal_text = f"""{tender['title']}

Organization: {tender['organization']}
Tender Value: {tender['value']}
Submission Deadline: {tender['deadline']}
Location: {tender['location']}
"""
                
                # Insert lead with high confidence (tenders are explicit)
                self.db.insert_lead(
                    company_id=company_id,
                    signal_text=signal_text,
                    signal_type='tender',
                    source_name=source['name'],
                    source_url=source['url'],
                    confidence=0.95
                )
                
                items_found += 1
                print(f"   ✅ Found: {tender['title'][:70]}...")
                print(f"      Value: {tender['value']} | Deadline: {tender['deadline']}")
        
        self.db.log_scrape(
            source_name=source['name'],
            source_type='tender',
            status='success',
            items_found=items_found
        )
        
        print(f"   📊 Total tenders found: {items_found}")
        return items_found
    
    def scrape_gem_portal(self, source):
        """
        Scrape GEM Portal
        Similar to CPP, GEM requires authentication
        Using sample data for demo
        """
        print(f"\n🏛️  Scraping: {source['name']}")
        print(f"   URL: {source['url']}")
        print("   ⚠️  Note: GEM Portal requires authentication")
        print("   Using representative sample data for demonstration")
        
        sample_orders = [
            {
                'title': 'Hexane (Technical Grade) for Solvent Extraction',
                'buyer': 'Food Corporation of India',
                'value': '₹35,00,000',
                'location': 'Multiple Locations'
            },
            {
                'title': 'Industrial Lubricants - Various Grades',
                'buyer': 'Defence Research and Development Organisation',
                'value': '₹45,00,000',
                'location': 'Delhi, Bangalore'
            }
        ]
        
        items_found = 0
        for order in sample_orders:
            if self.is_relevant(order['title']):
                company_id = self.db.insert_company(
                    name=order['buyer'],
                    industry='Government',
                    location=order['location']
                )
                
                signal_text = f"""{order['title']}

Buyer: {order['buyer']}
Order Value: {order['value']}
Location: {order['location']}
"""
                
                self.db.insert_lead(
                    company_id=company_id,
                    signal_text=signal_text,
                    signal_type='tender',
                    source_name=source['name'],
                    source_url=source['url'],
                    confidence=0.90
                )
                
                items_found += 1
                print(f"   ✅ Found: {order['title'][:70]}...")
        
        self.db.log_scrape(
            source_name=source['name'],
            source_type='tender',
            status='success',
            items_found=items_found
        )
        
        print(f"   📊 Total orders found: {items_found}")
        return items_found
    
    def scrape_all(self, sources):
        """Scrape all tender sources"""
        print("\n" + "=" * 70)
        print(f"🏛️  TENDER SCRAPING - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70)
        
        total_items = 0
        
        for source in sources:
            if not source.get('enabled', True):
                print(f"\n⏭️  Skipping (disabled): {source['name']}")
                continue
            
            # Route to appropriate scraper
            if 'CPP' in source['name']:
                items = self.scrape_cpp_portal(source)
            elif 'GEM' in source['name']:
                items = self.scrape_gem_portal(source)
            else:
                print(f"\n⚠️  No scraper implemented for: {source['name']}")
                items = 0
            
            total_items += items
        
        print("\n" + "─" * 70)
        print(f"📊 Total tender items found: {total_items}")
        print("=" * 70)
        print()
        
        return total_items
