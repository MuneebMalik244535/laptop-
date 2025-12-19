// import {themes as prismThemes} from 'prism-react-renderer';
// import type {Config} from '@docusaurus/types';
// import type * as Preset from '@docusaurus/preset-classic';

// // This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

// const config: Config = {
//   title: 'AI Humanoid Robots',
//   tagline: 'Advanced Robotics and AI Integration',
//   favicon: 'img/favicon.ico',

//   // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
//   future: {
//     v4: true, // Improve compatibility with the upcoming Docusaurus v4
//   },

//   // Set the production url of your site here
//   url: 'https://your-ai-humanoid-robotics-site.example.com',
//   // Set the /<baseUrl>/ pathname under which your site is served
//   // For GitHub pages deployment, it is often '/<projectName>/'
//   baseUrl: '/',

//   // GitHub pages deployment config.
//   // If you aren't using GitHub pages, you don't need these.
//   organizationName: 'my-org', // Usually your GitHub org/user name.
//   projectName: 'ai-humanoid-robots-book', // Usually your repo name.

//   onBrokenLinks: 'throw',

//   // Even if you don't use internationalization, you can use this field to set
//   // useful metadata like html lang. For example, if your site is Chinese, you
//   // may want to replace "en" with "zh-Hans".
//   i18n: {
//     defaultLocale: 'en',
//     locales: ['en'],
//   },

//   presets: [
//     [
//       'classic',
//       {
//         docs: {
//           sidebarPath: './sidebars.ts',
//           // Please change this to your repo.
//           // Remove this to remove the "edit this page" links.
//           editUrl:
//             'https://github.com/your-username/your-repo/tree/main/',
//         },
//         blog: {
//           showReadingTime: true,
//           feedOptions: {
//             type: ['rss', 'atom'],
//             xslt: true,
//           },
//           // Please change this to your repo.
//           // Remove this to remove the "edit this page" links.
//           editUrl:
//             'https://github.com/your-username/your-repo/tree/main/',
//           // Useful options to enforce blogging best practices
//           onInlineTags: 'warn',
//           onInlineAuthors: 'warn',
//           onUntruncatedBlogPosts: 'warn',
//         },
//         theme: {
//           customCss: './src/css/custom.css',
//         },
//       } satisfies Preset.Options,
//     ],
//   ],

//   themeConfig: {
//     // Replace with your project's social card
//     image: 'img/ai-humanoid-social-card.jpg',
//     colorMode: {
//       respectPrefersColorScheme: true,
//     },
//     navbar: {
//       title: 'AI Humanoid Robots',
//       logo: {
//         alt: 'AI Humanoid Robot Logo',
//         src: 'img/robot-logo.svg',
//       },
//       items: [
//         {
//           type: 'docSidebar',
//           sidebarId: 'tutorialSidebar',
//           position: 'left',
//           label: 'Chapters',
//         },
//         {to: '/blog', label: 'Blog', position: 'left'},
//         {
//           href: 'https://github.com/MuneebMalik244535/AI-Humanoid-Robotics-Books',
//           label: 'GitHub',
//           position: 'right',
//         },
//       ],
//     },
//     footer: {
//       style: 'dark',
//       links: [
//         {
//           title: 'Chapters',
//           items: [
//             {
//               label: 'Getting Started',
//               to: '/docs/intro',
//             },
//           ],
//         },
//         {
//           title: 'Community',
//           items: [
//             {
//               label: 'Robotics Stack Exchange',
//               href: 'https://robotics.stackexchange.com/',
//             },
//             {
//               label: 'AI Discord',
//               href: 'https://discord.gg/ai-research',
//             },
//             {
//               label: 'X',
//               href: 'https://x.com/ai_research',
//             },
//           ],
//         },
//         {
//           title: 'More',
//           items: [
//             {
//               label: 'Blog',
//               to: '/blog',
//             },
//             {
//               label: 'GitHub',
//               href: 'https://github.com/MuneebMalik244535/AI-Humanoid-Robotics-Books',
//             },
//           ],
//         },
//       ],
//       copyright: `Copyright © ${new Date().getFullYear()} AI Humanoid Robots Book. Built with Docusaurus.`,
//     },
//     prism: {
//       theme: prismThemes.github,
//       darkTheme: prismThemes.dracula,
//     },
//   } satisfies Preset.ThemeConfig,
// };

// export default config;






















// import {themes as prismThemes} from 'prism-react-renderer';
// import type {Config} from '@docusaurus/types';
// import type * as Preset from '@docusaurus/preset-classic';

// const config: Config = {
//   title: 'AI Humanoid Robots',
//   tagline: 'Advanced Robotics and AI Integration',
//   favicon: 'img/favicon.ico',

//   future: {
//     v4: true,
//   },

//   url: 'https://your-ai-humanoid-robotics-site.example.com',
//   baseUrl: '/',

//   organizationName: 'my-org',
//   projectName: 'ai-humanoid-robots-book',

//   onBrokenLinks: 'throw',

//   i18n: {
//     defaultLocale: 'en',
//     locales: ['en'],
//   },

//   presets: [
//     [
//       'classic',
//       {
//         docs: {
//           sidebarPath: './sidebars.ts',
//           editUrl:
//             'https://github.com/your-username/your-repo/tree/main/',
//         },

//         // ❌ DISABLE BLOG COMPLETELY
//         blog: false,

//         theme: {
//           customCss: './src/css/custom.css',
//         },
//       } satisfies Preset.Options,
//     ],
//   ],

//   themeConfig: {
//     image: 'img/ai-humanoid-social-card.jpg',
//     colorMode: {
//       respectPrefersColorScheme: true,
//     },
//     navbar: {
//       title: 'AI Humanoid Robots',
//       logo: {
//         alt: 'AI Humanoid Robot Logo',
//         src: 'img/robot-logo.svg',
//       },
//       items: [
//         {
//           type: 'docSidebar',
//           sidebarId: 'tutorialSidebar',
//           position: 'left',
//           label: 'Chapters',
//         },
//         // ❌ REMOVED BLOG LINK FROM NAVBAR
//         {
//           href: 'https://github.com/MuneebMalik244535/AI-Humanoid-Robotics-Books',
//           label: 'GitHub',
//           position: 'right',
//         },
//       ],
//     },

//     footer: {
//       style: 'dark',
//       links: [
//         {
//           title: 'Chapters',
//           items: [
//             {
//               label: 'Getting Started',
//               to: '/docs/intro',
//             },
//           ],
//         },
//         {
//           title: 'Community',
//           items: [
//             {
//               label: 'Robotics Stack Exchange',
//               href: 'https://robotics.stackexchange.com/',
//             },
//             {
//               label: 'AI Discord',
//               href: 'https://discord.gg/ai-research',
//             },
//             {
//               label: 'X',
//               href: 'https://x.com/ai_research',
//             },
//           ],
//         },
//         {
//           title: 'More',
//           items: [
//             // ❌ REMOVED BLOG LINK FROM FOOTER
//             {
//               label: 'GitHub',
//               href: 'https://github.com/MuneebMalik244535/AI-Humanoid-Robotics-Books',
//             },
//           ],
//         },
//       ],
//       copyright: `Copyright © ${new Date().getFullYear()} AI Humanoid Robots Book. Built with Docusaurus.`,
//     },

//     prism: {
//       theme: prismThemes.github,
//       darkTheme: prismThemes.dracula,
//     },
//   } satisfies Preset.ThemeConfig,

//   // Add custom root component to include chatbot across all pages
//   themes:
//   //  ['@docusaurus/theme-classic'],
//   plugins: [
//     async function myPlugin(context, options) {
//       return {
//         name: 'docusaurus-plugin-chatbot',
//         configureWebpack(config, isServer, utils) {
//           return {
//             resolve: {
//               alias: {
//                 path: require.resolve('path-browserify'),
//               },
//             },
//           };
//         },
//       };
//     },
//   ],
// };

// export default config;











import { themes as prismThemes } from 'prism-react-renderer';
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'AI Humanoid Robots',
  tagline: 'Advanced Robotics and AI Integration',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://your-ai-humanoid-robotics-site.example.com',
  baseUrl: '/',

  organizationName: 'my-org',
  projectName: 'ai-humanoid-robots-book',

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  // ✅ CLASSIC PRESET (theme already included — DO NOT add again)
  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          editUrl:
            'https://github.com/your-username/your-repo/tree/main/',
        },

        // ❌ Blog disabled completely
        blog: false,

        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/ai-humanoid-social-card.jpg',

    colorMode: {
      respectPrefersColorScheme: true,
    },

    navbar: {
      title: 'AI Humanoid Robots',
      logo: {
        alt: 'AI Humanoid Robot Logo',
        src: 'img/robot-logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Chapters',
        },
        {
          href: 'https://github.com/MuneebMalik244535/AI-Humanoid-Robotics-Books',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },

    footer: {
      style: 'dark',
      links: [
        {
          title: 'Chapters',
          items: [
            {
              label: 'Getting Started',
              to: '/docs/intro',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Robotics Stack Exchange',
              href: 'https://robotics.stackexchange.com/',
            },
            {
              label: 'AI Discord',
              href: 'https://discord.gg/ai-research',
            },
            {
              label: 'X',
              href: 'https://x.com/ai_research',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'GitHub',
              href:
                'https://github.com/MuneebMalik244535/AI-Humanoid-Robotics-Books',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} AI Humanoid Robots Book. Built with Docusaurus.`,
    },

    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,

  // ✅ ONLY custom plugin (NO themes key at all)
  plugins: [
    async function chatbotPlugin() {
      return {
        name: 'docusaurus-plugin-chatbot',
        configureWebpack() {
          return {
            resolve: {
              alias: {
                path: require.resolve('path-browserify'),
              },
            },
          };
        },
      };
    },
  ],
};

export default config;














