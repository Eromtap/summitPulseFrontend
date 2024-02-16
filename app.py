import streamlit as st
import asyncio
import time


conn = st.connection("postgresql", type="sql")

left, right = st.columns(2)

async def left_col():
    with left:
        st.markdown("#### Pulse Rate 1:")
        numbers = st.empty()        
        
        while 1:
            df = conn.query('SELECT * FROM heart_rates;', ttl="0")
            for row in df.itertuples():
                p1 = row.pulse1
            with numbers.container():
              st.write(p1)
              await asyncio.sleep(1)

async def right_col():
    with right:
        st.markdown("#### Pulse Rate 2:")
        numbers = st.empty()        
        
        while 1:
            df = conn.query('SELECT * FROM heart_rates;', ttl="0")
            for row in df.itertuples():
                p2 = row.pulse2
            with numbers.container():
              st.write(p2)
              await asyncio.sleep(1)



async def main():
    await asyncio.gather(right_col(), left_col())   


asyncio.run(main())


