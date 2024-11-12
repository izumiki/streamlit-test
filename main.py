import time

import streamlit as st 
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Display Image')
if st.checkbox('Show Image'):
    image = Image.open('DSCF2789.jpg')
    st.image(image, caption='Nagasaki', use_column_width=True)

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

st.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button: 
    right_column.write('ここは右カラム')

expandar1 = st.expander('問い合わせ1')
expandar1.write('問い合わせ1の回答')
expandar2 = st.expander('問い合わせ2')
expandar2.write('問い合わせ2の回答')
expandar3 = st.expander('問い合わせ')
expandar3.write('問い合わせ3の回答')

option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11))

)

'貴方の好きな数字は', option, 'です。'

text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味: ', text

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション: ', condition


st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40],
})

st.table(df.style.highlight_max(axis=0))

'''
# 章
## 節
### 項

``` python
import stleamlit as st
import numpy as np
import pandas as pd
```
'''

df = pd.DataFrame(
    np.random.rand(10, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)


