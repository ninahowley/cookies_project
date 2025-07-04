import streamlit as st
import pandas as pd 
import streamlit.components.v1
import base64

st.html("""<style>
[data-testid="stSidebar"]> div:first-child{
background-image: url("https://thumbs.dreamstime.com/b/chocolate-chip-cookies-crumbs-forming-vertical-frame-white-background-scattered-create-visually-appealing-clean-surface-352442146.jpg");
background-size: cover;
}
</style>""")

st.header(":cookie: Resources")

one, two, three, four = st.tabs(["Guide on Cookies", "Managing Cookies", "Browsing Cookies", "Tracking Pixels vs. Cookies"])


with one: 
     left, right = st.columns((1,2))
     with left:
          with open('cookiegif.gif', 'rb') as f:
               waving = f.read()
          data_url = base64.b64encode(waving).decode("utf-8")
          st.markdown(
          f'''
          <img src="data:image/gif;base64,{data_url}" alt="cat gif" style="display:block; margin:auto; height:200px;">
          ''',
          unsafe_allow_html=True,
          )
     with right:
          st.write("Here's the link to our comprehensive guide on cookies! If you ever want a little refresher on, for example, the different types of cookies, just revisit this guide! Also, feel free to share this with friends and family :sunglasses:")
          st.link_button("Click me!", "https://docs.google.com/presentation/d/1ptwSa7iPPFH59lXnABAMPUpgtUXNqvT1JhtzTnBm1uE/present?slide=id.g148f9c0646e_0_0")
     # streamlit.components.v1.iframe(src="https://docs.google.com/presentation/d/1ptwSa7iPPFH59lXnABAMPUpgtUXNqvT1JhtzTnBm1uE/edit?slide=id.g148f9c0646e_0_0", height=1000)


with two: 
     st.subheader("Want to manage your cookies directly on your browser?")
     st.markdown("**1.** Go to Settings > Privacy and security.")
     st.markdown("**2.** Delete browsing data (*Cookies and other site data* & *Cached images and files*) frequently to reduce tracking and remove outdated information.")
     st.markdown("**3.** Set your preferences for *Third-party cookies*. You can also choose to enable “send a 'Do not track' request with your browsing traffic”./" \
     "While this does not guarantee that your information will not be tracked, since the exact response depends on how the website interprets this request, it is still /" \
     "an extra protective guardrail against potential privacy violations.")



with three: 
     st.subheader("How should you navigate cookies when browsing websites?")
     st.markdown("**1.** Read cookie pop-ups and review your options before selecting your cookie preferences for each site you visit.")
     st.markdown("**2.** Only allow cookies on trusted websites.")
     st.write("**3.** Use browser extensions to manage cookies for you. These are particularly helpful for blocking third-party cookie /" \
     "pop-ups that may be more obscure.")

     st.link_button("Privacy Badger", "https://privacybadger.org/")
     st.link_button("Ghostery", "https://www.ghostery.com/")

with four: 
     left, right = st.columns([1,2])
     with left:
         st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)  # Adds vertical space
         st.caption("Third party cookies are bad but maybe not the worst...")
         st.subheader("Be careful of tracking pixels!")
     with right:
          st.image("tracking pixel image.png", width = 1000) #HOOOOWW do I center this omg
     
     c1, c2, c3 = st.columns(3)
     c1.subheader("WHAT?")
     c1. write("Also known as a **web beacon**, a tracking pixel is a small, transparent image that a website operator adds to the HTML code of an email or ad.")
     c2.subheader("WHY?")
     c2.write("These pixels can track how often you visit a specific webpage, your IP addresses, device types, browsers, geographic locations, even when you submit a form or make a purchase...")
     c3.subheader("**HOW?**")
     c3.write("After a user loads a webpage, the browser reads the HTML code and sends a request to an external server. THe server then records the interaction and captures various user data points.")


     st.subheader("Tracking Pixels vs. Cookies") #How can I center this lol
     df = pd.DataFrame(
          {
               "Aspect": ["Purpose", "Location", "Management"],
               "Cookies": ["Store user data and preferences",
                           "Information is stored on the user’s device",
                           "User can choose when to clear (first-party) cookies and what to clear"],
               "Tracking Pixels": ["Monitor interactions and gather data",
                          "Information is sent to an external server directly",
                          "User cannot easily disable pixels and is often unaware of being tracked"]
          }
     )

     st.dataframe(df, hide_index=True)

     st.subheader("So...what should we do?")
     st.markdown("**1.** Disable automatic image loading on your email.")
     st.image("blocktracking.png", caption="Only click 'show images' if it's necessary, or if you trust the sender!")
     st.markdown("**2.** Browse in incognito  mode when you can.")
     st.markdown("**3.** Be very mindful of what you choose to click and open.")
     st.markdown("**4.** Use browser extensions to help block tracking pixels.")
     st.link_button("Ugly Email Browser Extension", "https://uglyemail.com/")

# with five:
#      st.header("Research")
     
#      st.write("**[An Empirical Study of Web Cookies](%s)**" % "https://dl.acm.org/doi/abs/10.1145/2872427.2882991#abstract")
#      st.write("**[HTTP Cookies: Standards, privacy, and politics](%s)**" %"https://dl.acm.org/doi/abs/10.1145/502152.502153#abstract")
#      st.write("**[CookieGraph: Understanding and Detecting First-Party Tracking Cookies](%s)**" %"https://dl.acm.org/doi/abs/10.1145/3576915.3616586#abstract")

#      st.header("Articles")
     
#      st.write("**[This Article Is Spying on You](%s)**" %"https://www.nytimes.com/2019/09/18/opinion/data-privacy-tracking.html")
#      st.write("**[All You Need to Know About Third-Party Cookies](%s)**" %"https://cookie-script.com/all-you-need-to-know-about-third-party-cookies.html")

#      st.write()
#      st.write("Need to add citations")