#!/usr/bin/env python3
"""
Automated Translation Tool for LinkedIn Quiz Files
Translates quiz markdown files to multiple languages
"""

import sys
import time
from pathlib import Path
from deep_translator import GoogleTranslator

# Language configurations with codes
LANGUAGES = {
    '1': {'name': 'Chinese (Simplified)', 'code': 'zh-CN', 'suffix': 'zh-CN'},
    '2': {'name': 'Chinese (Traditional)', 'code': 'zh-TW', 'suffix': 'zh-TW'},
    '3': {'name': 'Spanish', 'code': 'es', 'suffix': 'es'},
    '4': {'name': 'French', 'code': 'fr', 'suffix': 'fr'},
    '5': {'name': 'Portuguese', 'code': 'pt', 'suffix': 'pt'},
    '6': {'name': 'German', 'code': 'de', 'suffix': 'de'},
    '7': {'name': 'Japanese', 'code': 'ja', 'suffix': 'ja'},
    '8': {'name': 'Korean', 'code': 'ko', 'suffix': 'ko'},
    '9': {'name': 'Russian', 'code': 'ru', 'suffix': 'ru'},
    '10': {'name': 'Italian', 'code': 'it', 'suffix': 'it'},
    '11': {'name': 'Arabic', 'code': 'ar', 'suffix': 'ar'},
    '12': {'name': 'Hindi', 'code': 'hi', 'suffix': 'hi'},
    '13': {'name': 'Turkish', 'code': 'tr', 'suffix': 'tr'},
    '14': {'name': 'Vietnamese', 'code': 'vi', 'suffix': 'vi'},
    '15': {'name': 'Polish', 'code': 'pl', 'suffix': 'pl'},
    '16': {'name': 'Dutch', 'code': 'nl', 'suffix': 'nl'},
    '17': {'name': 'Indonesian', 'code': 'id', 'suffix': 'id'},
    '18': {'name': 'Thai', 'code': 'th', 'suffix': 'th'},
    '19': {'name': 'Swedish', 'code': 'sv', 'suffix': 'sv'},
    '20': {'name': 'Greek', 'code': 'el', 'suffix': 'el'},
}

def show_languages():
    """Display all available languages"""
    print("\n" + "=" * 70)
    print("Select target language:")
    print("=" * 70)
    
    for key, lang in sorted(LANGUAGES.items(), key=lambda x: int(x[0])):
        print(f"  {key:2}. {lang['name']}")
    
    print("\nEnter choice (1-20): ", end='')

def get_file_path():
    """Get quiz file path from user"""
    print("=" * 70)
    print("LinkedIn Quiz Translation Tool")
    print("=" * 70)
    print("\nEnter the quiz file path to translate")
    print("Example: xml/xml-quiz.md")
    print("         python/python-quiz.md")
    print("\nFile path: ", end='')
    
    file_path = input().strip()
    
    # Convert to Path object
    path = Path(file_path)
    
    if not path.exists():
        print(f"\n❌ Error: File '{file_path}' not found!")
        sys.exit(1)
    
    if not path.suffix == '.md':
        print(f"\n❌ Error: File must be a .md file!")
        sys.exit(1)
    
    return path

def select_language():
    """Interactive language selection"""
    show_languages()
    choice = input().strip()
    
    if choice not in LANGUAGES:
        print("❌ Invalid choice!")
        sys.exit(1)
    
    return LANGUAGES[choice]

def translate_text(text, target_lang_code, max_length=4500):
    """Translate text using Google Translate"""
    try:
        if len(text) > max_length:
            # Split into smaller chunks
            chunks = []
            current = ""
            
            for line in text.split('\n'):
                if len(current) + len(line) < max_length:
                    current += line + '\n'
                else:
                    if current:
                        chunks.append(current)
                    current = line + '\n'
            
            if current:
                chunks.append(current)
            
            # Translate each chunk
            translated_chunks = []
            for chunk in chunks:
                translator = GoogleTranslator(source='en', target=target_lang_code)
                translated = translator.translate(chunk)
                translated_chunks.append(translated)
                time.sleep(0.5)
            
            return '\n'.join(translated_chunks)
        else:
            translator = GoogleTranslator(source='en', target=target_lang_code)
            return translator.translate(text)
    
    except Exception as e:
        print(f"\n❌ Translation error: {e}")
        return None

def translate_file(input_path, lang_config):
    """Translate the quiz file"""
    print(f"\n{'='*70}")
    print(f"Translating to {lang_config['name']}...")
    print('='*70)
    
    # Read input file
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\n📄 Input: {input_path}")
    print(f"📊 Size: {len(content)} characters")
    
    # Generate output filename
    # Example: xml/xml-quiz.md -> xml/xml-quiz.fr.md
    output_path = input_path.parent / f"{input_path.stem}.{lang_config['suffix']}{input_path.suffix}"
    
    print(f"📝 Output: {output_path}")
    
    # Split into chunks
    chunks = []
    current_chunk = ""
    in_code_block = False
    
    for line in content.split('\n'):
        # Detect code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
        
        if in_code_block or len(current_chunk) + len(line) < 4000:
            current_chunk += line + '\n'
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = line + '\n'
    
    if current_chunk:
        chunks.append(current_chunk)
    
    print(f"📦 Split into {len(chunks)} chunks")
    print(f"\n🔄 Translating...\n")
    
    # Translate each chunk
    translated_chunks = []
    
    for i, chunk in enumerate(chunks, 1):
        print(f"[{i}/{len(chunks)}] Chunk {i}... ", end='', flush=True)
        
        translated = translate_text(chunk, lang_config['code'])
        
        if translated:
            translated_chunks.append(translated)
            print(f"✅")
        else:
            print("❌ Failed!")
            return False
        
        time.sleep(1)
    
    # Combine
    final_translation = '\n'.join(translated_chunks)
    
    # Save
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_translation)
    
    print(f"\n{'='*70}")
    print(f"✅ Translation complete!")
    print(f"📝 Saved to: {output_path}")
    print(f"📊 Size: {len(final_translation)} characters")
    print('='*70)
    
    return True

def main():
    # Check if deep-translator is installed
    try:
        from deep_translator import GoogleTranslator
    except ImportError:
        print("=" * 70)
        print("❌ deep-translator not installed!")
        print("=" * 70)
        print("\n📦 Install with:")
        print("   pip install deep-translator")
        print("\nThen run this script again.")
        sys.exit(1)
    
    # Get file path
    input_path = get_file_path()
    
    # Select language
    lang_config = select_language()
    
    print(f"\n✨ Selected: {lang_config['name']}")
    print(f"📁 Input: {input_path}")
    print(f"📁 Output: {input_path.parent / f'{input_path.stem}.{lang_config['suffix']}{input_path.suffix}'}")
    
    # Confirm
    print(f"\nProceed with translation? (y/n): ", end='')
    confirm = input().strip().lower()
    
    if confirm != 'y':
        print("❌ Cancelled")
        sys.exit(0)
    
    # Translate
    success = translate_file(input_path, lang_config)
    
    if success:
        print(f"\n🎉 Success!")
        print(f"\n💡 Next steps:")
        print(f"   1. Review the translated file")
        print(f"   2. git add {input_path.parent}/*.{lang_config['suffix']}.md")
        print(f"   3. git commit -m 'Add {lang_config['name']} translation'")
        print(f"   4. Create PR")
    else:
        print("\n❌ Translation failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
