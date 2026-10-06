import streamlit as st
import numpy as np
from starter import ZONES, TIME_BLOCKS, COSTS, delivery_times


def cost_late(cost):
  refund = cost['refund']
  churn = cost['churn_orders']
  margin = cost['margin']
  total_cost = refund+margin*churn
  return total_cost


def best_promise(zone, time_block, promises, costs):
  best_p = 0
  highest_profit = 0
  for promise in promises:
    total = 0
    late = 0
    orders = delivery_times(zone, time_block, promise, seed = 1)
    for order in orders:
      total += costs['margin']
      if order > promise:
        late += cost_late(costs)
    net_profit = round(total-late, 2)
    if highest_profit < net_profit:
      best_p = promise
      highest_profit = net_profit
  return best_p, highest_profit


st.title("Rosa's Pizza: Best Delivery Promise")

zone = st.selectbox("Zone", ZONES)
time_block = st.selectbox("Time block", TIME_BLOCKS)

st.subheader("Promise range (minutes)")
col1, col2, col3 = st.columns(3)
start = col1.number_input("Start", min_value=1, value=5, step=1)
end = col2.number_input("End", min_value=1, value=75, step=1)
step = col3.number_input("Step", min_value=1, value=5, step=1)

st.subheader("Costs")
margin = st.number_input("Profit margin per order ($)", min_value=0.0,
                         value=float(COSTS['margin']), step=0.5)
churn = st.number_input("Churn per late order (lost future orders)",
                        min_value=0.0, value=float(COSTS['churn_orders']),
                        step=0.1)
refund = st.number_input("Refund per late order ($)", min_value=0.0,
                         value=float(COSTS['refund']), step=0.5)

if st.button("Find best promise"):
  if end < start:
    st.error("End must be greater than or equal to start.")
  else:
    promises = list(range(int(start), int(end) + 1, int(step)))
    costs = {'refund': refund, 'churn_orders': churn, 'margin': margin}
    best_p, highest_profit = best_promise(zone, time_block, promises, costs)
    if best_p == 0:
      st.warning("No promise in this range is profitable.")
    else:
      st.success(f"Recommended promise: {best_p} min "
                 f"(net profit ${highest_profit:,.2f})")
