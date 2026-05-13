from kivy.lang import Builder

kv = '''
BoxLayout:
    Label: text: 'Item'; bold: True; height: 35; size_hint_y: None
'''

try:
    Builder.load_string(kv)
    print("SUCCESS")
except Exception as e:
    print("FAILED:", e)
