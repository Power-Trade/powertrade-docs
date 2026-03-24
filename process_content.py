#!/usr/bin/env python3
"""
Process the PowerTrade FAQ content and organize it into Docusaurus structure
"""

import re
import os
from pathlib import Path

def clean_content(text):
    """Clean up PDF conversion artifacts"""
    # Remove page headers/footers with timestamps
    text = re.sub(r'3/23/26, 11:24 PM Power Trade Guides and FAQ\d*', '', text)
    
    # Remove excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Fix common formatting issues
    text = text.replace('|', '')
    text = text.replace('ʼ', "'")
    text = text.replace(''', "'")
    text = text.replace('"', '"')
    text = text.replace('"', '"')
    
    # Clean up bullet points
    text = re.sub(r'^(\d+)\.\s+', r'1. ', text, flags=re.MULTILINE)
    
    return text.strip()

def extract_sections(content):
    """Extract main sections from the content"""
    
    # Split content into logical sections
    sections = {}
    
    # Define section patterns
    section_patterns = {
        'intro': r'Power Trade Guides and FAQ.*?(?=How to use PowerTrade)',
        'how-to-use': r'How to use PowerTrade.*?(?=Trading)',
        'trading': r'Trading(?:\s|\n).*?(?=Legal)',
        'legal': r'Legal(?:\s|\n).*?$'
    }
    
    for section_name, pattern in section_patterns.items():
        match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
        if match:
            sections[section_name] = clean_content(match.group(0))
    
    return sections

def create_getting_started_content():
    return """# Getting Started

Welcome to PowerTrade! This guide will help you get started with our cryptocurrency trading platform.

## What is PowerTrade?

At **PowerTrade**, we're a team of crypto-native professionals and tech builders passionate about shaping the future of crypto trading. Our mission is to empower institutional firms and professional traders with a powerful, intuitive platform to access the fast-moving world of crypto derivatives.

We're obsessed with user experience, driven by innovation, and committed to building tools that make trading crypto options, perpetuals, and structured products seamless. Whether you're executing complex strategies or trading high-volume block trades, PowerTrade is built to support your edge.

## Services we offer

At PowerTrade, we provide a comprehensive suite of services designed to cater to the diverse needs of institutional firms and professional traders in the crypto derivatives market:

1. **Crypto Options Trading:** Trade USD-settled, European-style options on BTC, ETH, and 80+ altcoins — more than any other platform.
2. **Perpetuals, Futures, and Spot Markets:** Access deep liquidity across perpetual contracts, futures, and spot pairs for dynamic portfolio management.
3. **Request-for-Quote (RFQ) System:** Execute block trades or build multi-leg structures with our Request-for-Quote interface — fast, secure, and anonymous.
4. **Multi-Leg Strategies:** Execute complex trading strategies by combining multiple options contracts with different strike prices and expiration dates.
5. **One-click strategies builder:** Select your bullish, rangebound or bearish strategy with these pre-built strategies.
6. **Short-term expiration, "DEGEN" options:** Enjoy 10-minute and 1-hour expiration options, with no liquidation risk, for selected tokens.
7. **Desktop and Mobile Applications:** Enjoy a seamless trading experience across devices with our desktop application and mobile apps for iOS and Android.
8. **API Access:** Integrate your trading tools and algorithms with our platform using our API.
9. **Competitive Fee Structure:** Take advantage of our competitive fees, designed to help you maximize your trading profits.

## Where to find the PowerTrade app

The PowerTrade app is currently available on iOS, Android and web app.

*Please note that the app is not available in [certain countries](../legal/country-availability).*

### iOS
The iOS app is live and can be found [on the iOS App store](https://apps.apple.com/us/app/powertrade/id1548085709).

### Android
Our Android app is live and can be found [on the Google Play store](https://play.google.com/store/apps/details?id=com.pt.powertrade).

### Web
Our web application can be accessed at https://app.power.trade/

## Next Steps

- [Sign Up for an Account](sign-up) - Create your PowerTrade account
- [Account Verification](account-verification) - Complete KYC process
- [Make a Deposit](deposits) - Fund your account
- [Start Trading](../trading/options) - Begin with options trading

## Still have questions?

- **Email Support:** support@power.trade
- **Telegram:** https://t.me/power_trade"""

def process_content_file():
    """Main processing function"""
    
    # Read the content file
    content_file = Path('/home/jenkins/.openclaw/media/inbound/PowerTrade_FAQ---0ad979fe-587d-4ca3-b51f-f6026b964677.txt')
    
    with open(content_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create the main getting started content
    getting_started_content = create_getting_started_content()
    
    # Write the getting started file
    with open('docs/how-to-use-powertrade/getting-started.md', 'w', encoding='utf-8') as f:
        f.write(getting_started_content)
    
    # Create a simple sign-up guide
    signup_content = """# Sign Up for a PowerTrade Account

Create your PowerTrade account in minutes. Step-by-step signup for trading BTC, ETH, altcoin options & perpetuals.

## Quick Start Guide

Welcome to PowerTrade! The following guide will walk you through signing up for a new account to trade cryptocurrency derivatives.

### Step 1: Get Started
Tap the "Get Started" button to begin.

### Step 2: Enter Email
Enter your email address and tap the "Sign Up" button. This will trigger a confirmation email to be sent to you.

### Step 3: Confirm Email
Tap on the "Login to PowerTrade" button or the magic link to be logged in to the PowerTrade app. You must do this on the same device that the PowerTrade app is installed on for this magic link to work. The link will expire if it is not used within 1 hour.

### Step 4: Personal Information
Since this is the first time you're logging in on this newly-created account, we will ask you for a few pieces of personal information. This information will only be used for the administration of PowerTrade services, account recovery and will not be shared with marketing partners without your consent.

Input your full legal name and tap on "Save".

### Step 5: Terms & Conditions
Tick on the check box and tap on the "Continue" button.

### Step 6: Security PIN
Create a 4 digit security PIN when prompted to do so. This PIN is tied to this device and to this sign in session, so you will be asked to create a new PIN if you log out and log back in.

### Congratulations! 
You have successfully created an account and can now proceed to fund your account and trade cryptocurrency derivatives on PowerTrade!

## Next Steps

- [Verify Your Account](account-verification) - Complete KYC for higher limits
- [Make a Deposit](deposits) - Fund your trading account
- [Security Tips](security-tips) - Keep your account safe

## Still have questions?

- **Email Support:** support@power.trade
- **Telegram:** https://t.me/power_trade"""

    with open('docs/how-to-use-powertrade/sign-up.md', 'w', encoding='utf-8') as f:
        f.write(signup_content)
    
    print("✅ Content processing completed!")
    print("📁 Created structured content in docs/ directory")
    print("🚀 Ready for Docusaurus build!")

if __name__ == "__main__":
    process_content_file()