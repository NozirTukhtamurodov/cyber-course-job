#!/bin/bash

# Compile translation files
echo "📝 Compiling translation files..."

msgfmt src/locales/en/LC_MESSAGES/messages.po -o src/locales/en/LC_MESSAGES/messages.mo
msgfmt src/locales/uz/LC_MESSAGES/messages.po -o src/locales/uz/LC_MESSAGES/messages.mo

echo "✅ Translation files compiled successfully!"
