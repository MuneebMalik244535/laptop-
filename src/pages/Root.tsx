import React from 'react';
import Chatbot from '../components/Chatbot/Chatbot';

export default function Root({ children }) {
  return (
    <>
      {children}
      <Chatbot />
    </>
  );
}