#!/usr/bin/env python3
"""
Simple content processor for PowerTrade FAQ
"""

def create_key_pages():
    """Create the most important pages manually"""
    
    # Update getting started with real content
    getting_started = """# Getting Started

Welcome to PowerTrade! This guide will help you get started with our cryptocurrency trading platform.

## What is PowerTrade?

At **PowerTrade**, we're a team of crypto-native professionals and tech builders passionate about shaping the future of crypto trading. Our mission is to empower institutional firms and professional traders with a powerful, intuitive platform to access the fast-moving world of crypto derivatives.

## Services we offer

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

### iOS
The iOS app is live and can be found [on the iOS App store](https://apps.apple.com/us/app/powertrade/id1548085709).

### Android
Our Android app is live and can be found [on the Google Play store](https://play.google.com/store/apps/details?id=com.pt.powertrade).

### Web
Our web application can be accessed at https://app.power.trade/

## Next Steps

- [Account Verification](account-verification) - Complete KYC process
- [Make a Deposit](deposits) - Fund your account  
- [Start Trading](../trading/options) - Begin with options trading

## Still have questions?

- **Email Support:** support@power.trade
- **Telegram:** https://t.me/power_trade"""

    # Create deposits guide  
    deposits = """# Deposits on PowerTrade

Learn how to deposit USDC, BTC, ETH and altcoins safely into PowerTrade. Supported assets, confirmations and tips.

## Supported Assets

Users can fund their trading accounts with:
- ERC20 USDC tokens
- Bitcoin (BTC)
- Ethereum (ETH) 
- PowerTrade Fuel (PTF)
- Solana (SOL)
- Avalanche (AVAX)
- Binance Coin (BNB)
- Dogecoin (DOGE)
- Chainlink (LINK)
- Litecoin (LTC)
- SUI Network (SUI)
- Toncoin (TON)
- Ripple (XRP)

## How to Deposit (Web)

1. Go to your Funds screen by clicking on the menu dropdown in the top navigation and select "Deposit Add funds"
2. Click on the "Deposit" button next to the asset you want to deposit
3. Your PowerTrade wallet address will be revealed. You can also click the QR code icon to see your wallet's address in QR code form
4. Send funds from your external wallet to this address

**Important:** Make sure to only transfer the correct type of asset into the wallet. Transferring the wrong type of cryptocurrency may render it unrecoverable!

## How to Deposit (Mobile)

1. Tap on the Wallet icon on your app
2. Select the cryptocurrency you intend to use
3. Tap on the "Deposit" button to reveal your PowerTrade wallet address  
4. You can also tap on the QR code icon to reveal your wallet's address in QR code form
5. Send funds from your external wallet

## Confirmation

Once the transaction is confirmed on the blockchain, your wallet balance will be updated. You will also receive an email confirmation of the transaction.

## Troubleshooting Delayed Deposits

Common causes of delays:
- **Transaction wasn't broadcast** - Check if your transaction appears on the blockchain explorer
- **Network Congestion** - High traffic can delay processing
- **Low fees** - Transactions with higher fees get priority
- **Prior unconfirmed transactions** - Wait for previous transactions to confirm

## Still have questions?

- **Email Support:** support@power.trade
- **Telegram:** https://t.me/power_trade"""

    # Options trading intro
    options = """# Options Trading on PowerTrade

Learn to trade crypto options. Calls, puts, spreads & hedges for BTC, ETH and 80+ altcoin markets.

## What Are Crypto Options?

Crypto options are financial derivatives that give traders the right, but not the obligation, to buy or sell an underlying cryptocurrency at a fixed price (the strike price) on or before a specific date.

Unlike spot trading or perpetual futures, options allow you to limit your downside while keeping unlimited upside potential. On PowerTrade, all options are European-style and settled in USDC.

## Call Options

A call option gives the buyer the right (not the obligation) to buy the cryptocurrency at the strike price.

- Traders buy calls when they expect the crypto price to rise
- Profit potential is unlimited if the price moves above the strike price

**Example:** A trader buys a BTC call option with a $50,000 strike price. If BTC rises to $55,000 before expiry, the trader can buy at $50,000 and capture the $5,000 difference (minus the premium).

## Put Options  

A put option gives the buyer the right (not the obligation) to sell the cryptocurrency at the strike price.

- Traders buy puts when they expect the crypto price to fall
- Useful for hedging against downside risk

**Example:** A trader buys an ETH put option with a $3,000 strike price. If ETH drops to $2,500, the trader can sell at $3,000, profiting $500 (minus the premium).

## European Style Options

PowerTrade offers European-style options, which can only be exercised at the expiration date. This structure:

- Prevents early exercise risk
- Simplifies strategy planning  
- Keeps the focus on price moves up to expiry

## USDC Cash-Settled Options

All PowerTrade options are cash-settled in USDC:

- No need to hold BTC, ETH, or altcoins directly
- Settlement in stable USDC makes it easy to manage profits and losses
- Reduces custody risk compared to physically settled options

## Why Trade Options on PowerTrade?

- ✅ 80+ altcoin options markets (the most in crypto)
- ✅ Tight pricing & deep liquidity
- ✅ Risk-defined strategies with capped downside
- ✅ Flexible expirations — daily to 3 months forward
- ✅ Simple settlement in USDC

## Get Started Today

- **Email Support:** support@power.trade
- **Telegram:** https://t.me/power_trade  
- **Start Trading:** [PowerTrade App](https://app.power.trade)"""

    # Write the files
    with open('docs/how-to-use-powertrade/getting-started.md', 'w') as f:
        f.write(getting_started)
    
    with open('docs/how-to-use-powertrade/deposits.md', 'w') as f:
        f.write(deposits)
        
    with open('docs/trading/options.md', 'w') as f:
        f.write(options)
    
    print("✅ Created key content pages!")
    print("📁 Files updated:")
    print("   - docs/how-to-use-powertrade/getting-started.md")  
    print("   - docs/how-to-use-powertrade/deposits.md")
    print("   - docs/trading/options.md")

if __name__ == "__main__":
    create_key_pages()