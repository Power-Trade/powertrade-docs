import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  // Main sidebar for docs
  mainSidebar: [
    {
      type: 'doc',
      id: 'intro',
      label: 'Introduction',
    },
    {
      type: 'category',
      label: 'How to use PowerTrade',
      collapsed: false,
      items: [
        'how-to-use-powertrade/getting-started',
        'how-to-use-powertrade/login',
        'how-to-use-powertrade/email-issues',
        'how-to-use-powertrade/subaccounts',
        'how-to-use-powertrade/security-tips',
        'how-to-use-powertrade/deposits',
        'how-to-use-powertrade/withdrawals',
        'how-to-use-powertrade/account-verification',
        'how-to-use-powertrade/corporate-accounts',
        'how-to-use-powertrade/fees',
      ],
    },
    {
      type: 'category',
      label: 'Trading',
      collapsed: false,
      items: [
        'trading/options',
        'trading/options-btc',
        'trading/options-bnb',
        'trading/options-doge',
        'trading/futures',
        'trading/margin-and-liquidation',
        'trading/perpetuals',
        'trading/spot',
        'trading/api',
        'trading/xstocks-tokenized-stocks',
      ],
    },
    {
      type: 'category',
      label: 'Legal',
      collapsed: false,
      items: [
        'legal/legal-and-privacy-policies',
        'legal/country-availability',
        'legal/risk-disclosure',
        'legal/security',
        'legal/whitepaper',
      ],
    },
  ],
};

export default sidebars;