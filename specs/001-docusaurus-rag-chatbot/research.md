# Research: Docusaurus RAG Chatbot Integration

## Phase 0: Technical Research and Decision Summary

### 1. Technology Stack Research

#### Decision: Frontend Framework
- **Rationale**: Using React 18 with Docusaurus 3 for seamless integration with the existing documentation site. Docusaurus itself is built on React, making it a natural choice for adding custom UI components.
- **Alternatives considered**: Vanilla JavaScript, Vue.js, Angular
- **Chosen because**: Best integration with Docusaurus, strong component ecosystem, team familiarity

#### Decision: Styling Solution
- **Rationale**: Using Tailwind CSS for component styling due to its utility-first approach that enables rapid development of custom UI components like the floating button and chat interface.
- **Alternatives considered**: Styled-components, CSS Modules, Material UI
- **Chosen because**: Minimal CSS footprint, utility classes work well for custom UI, good performance

#### Decision: Backend Framework
- **Rationale**: FastAPI selected for the backend due to its high performance, built-in support for async operations, excellent documentation, and strong integration with Python data science ecosystem.
- **Alternatives considered**: Flask, Django, Node.js/Express
- **Chosen because**: Performance requirements, async support for AI operations, automatic API docs generation

#### Decision: Vector Database Client
- **Rationale**: Using the official Qdrant Python client for connecting to Qdrant Cloud, which provides the vector search capabilities needed for the RAG pipeline.
- **Alternatives considered**: PyMongo, Weaviate client, Elasticsearch
- **Chosen because**: Required by specification, specifically for Qdrant Cloud integration

#### Decision: SQL Database Client
- **Rationale**: Using the Neon Postgres driver for connecting to Neon Serverless Postgres, which stores the metadata and full JSON chapters as specified.
- **Alternatives considered**: SQLAlchemy, asyncpg
- **Chosen because**: Required by specification, specifically for Neon Postgres integration

#### Decision: AI Processing SDK
- **Rationale**: Using OpenAI SDK for connecting to OpenAI services for the final answer generation in the RAG pipeline.
- **Alternatives considered**: HuggingFace Transformers, LangChain, Anthropic SDK
- **Chosen because**: Required by specification, proven reliability and quality

### 2. Component Architecture Research

#### Decision: Floating Button Implementation
- **Rationale**: Creating a React component that renders as a fixed-position floating action button (FAB) in the bottom-right corner of the page, following Material Design patterns but with custom styling to match the book brand.
- **Implementation approach**: 
  - Use React with TypeScript
  - Implement as a portal to ensure it's always visible above other content
  - Use CSS transitions for animation
- **Alternatives considered**: Using a pre-built FAB library vs. custom implementation
- **Chosen because**: Full control over appearance and behavior, minimal bundle size impact

#### Decision: Chat Interface Implementation
- **Rationale**: Creating a React component with a slide-up animation when the floating button is clicked, containing a message history area and input field.
- **Implementation approach**:
  - Use React hooks for state management
  - Implement message history with auto-scrolling
  - Include typing indicators and error states
- **Alternatives considered**: Custom chat widget vs. existing chat libraries
- **Chosen because**: Custom implementation required for domain-specific intelligence, better control over privacy

### 3. API Design Research

#### Decision: Backend API Endpoints
- **Rationale**: Following REST conventions with three required endpoints as specified in the feature requirements: /query, /select-text, /health.
- **Implementation approach**:
  - /query: Accepts user questions and returns RAG-generated answers
  - /select-text: Processes user-selected text for context
  - /health: Returns system status information
- **Alternatives considered**: GraphQL vs. REST
- **Chosen because**: REST required by specification

### 4. Performance and Bundle Size Considerations

#### Decision: Minimize Frontend Impact
- **Rationale**: To meet the requirement of minimal CSS/JS impact on the existing Docusaurus site performance.
- **Implementation approach**:
  - Code splitting for chat components
  - Lazy loading of chat interface
  - Tree-shaking of unused dependencies
  - <100KB bundle size impact target
- **Alternatives considered**: Heavy chat widget vs. lightweight custom solution
- **Chosen because**: Performance requirements from specification

### 5. Security and Privacy Research

#### Decision: Privacy-First Implementation
- **Rationale**: Following the "Privacy by Design" constitutional principle, ensuring no unnecessary data is stored or transmitted.
- **Implementation approach**:
  - Do not store user queries by default
  - Implement opt-in analytics if needed
  - Use secure connections (HTTPS) for all API calls
  - Clear chat history when user closes the interface
- **Alternatives considered**: Persistent chat history vs. ephemeral sessions
- **Chosen because**: Privacy constitutional requirement

### 6. Error Handling and Fallbacks

#### Decision: Graceful Error Handling
- **Rationale**: Following FR-010 to handle errors gracefully when backend services are unavailable.
- **Implementation approach**:
  - Show user-friendly error messages when services are down
  - Implement retry logic with exponential backoff
  - Provide offline/cached fallback options if possible
- **Alternatives considered**: Disable chat interface vs. error messages
- **Chosen because**: User experience requirement to inform rather than break silently