import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Power Trade Guides and FAQ',
  tagline: 'Learning resources to get you started using PowerTrade',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://power-trade.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/powertrade-docs/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'Power-Trade', // Usually your GitHub org/user name.
  projectName: 'powertrade-docs', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: '/', // Serve docs at site's root
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/Power-Trade/powertrade-docs/tree/main/',
        },
        blog: false, // Disable blog
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'Power Trade Support',
      logo: {
        alt: 'Power Trade Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          href: 'https://power.trade',
          label: 'Main Site',
          position: 'right',
        },
        {
          href: 'https://github.com/Power-Trade/powertrade-docs',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Support',
          items: [
            {
              label: 'Email Support',
              href: 'mailto:support@power.trade',
            },
            {
              label: 'Telegram',
              href: 'https://t.me/power_trade',
            },
          ],
        },
        {
          title: 'Power Trade',
          items: [
            {
              label: 'Main Site',
              href: 'https://power.trade',
            },
            {
              label: 'Trading Platform',
              href: 'https://app.power.trade',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Power Trade. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
    algolia: {
      // The application ID provided by Algolia
      appId: 'YOUR_APP_ID', // Replace when you set up search
      // Public API key: it is safe to commit it
      apiKey: 'YOUR_SEARCH_API_KEY',
      indexName: 'powertrade-docs',
      // Optional: see doc section below
      contextualSearch: true,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;