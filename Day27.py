# Day 27 — Web Fundamentals 


# Aaj hum samjhenge ki browser aur web server aapas mein kaise communicate karte hain, URL ke parts kya hote hain, aur HTTP headers, cookies, sessions aur caching ka web security se kya connection hai.

# Tum Day 20 par HTTP/HTTPS aur DevTools padh chuke ho, isliye aaj usi ko thoda deeper level par revise karenge.


# 1. Browser aur Web Server

# Browser (Client)
# Chrome, Firefox, Edge
#       ↑
# HTTP Request
# GET /index.html, headers, cookies
#       ↓
# HTTP Response
# Status code, headers, HTML/data

# Web Server
# Request process karta hai aur response bhejta hai


# - Browser: Website ko access aur display karta hai.
# - Web server: Browser ki request receive karke response deta hai.
# - HTTP: Communication protocol hai.
# - HTTPS: HTTP ko TLS encryption ke saath use karta hai, jisse transit mein data ki confidentiality aur integrity protect hoti hai.

# Example: Tum Chrome mein https://example.com open karte ho. Browser server se request karta hai aur server HTML ya doosra response bhejta hai.


# 2. URL ke parts samjho
# Example URL:
# https://example.com:443/search?q=cyber&level=beginner#results

# Protocol / Scheme
# https://

# Domain / Host
# example.com

# Port (optional)
# :443

# Path
# /search

# Query string
# ?q=cyber&level=beginner

# Fragment
# #results

# Part	        Meaning

# Protocol	    Browser aur server ke communication ka tareeka
# Domain	    Server ka human-readable address
# Port	        Service tak pahunchne ka port; HTTPS ka default port 443 hai
# Path	        Server par requested resource ya route
# Query string	? ke baad key-value parameters
# Fragment	    # ke baad page ka section; aam taur par server ko HTTP request mein nahi bheja jata

# Cybersecurity tip: Query string mein password, OTP, API key ya sensitive personal information nahi rakhni chahiye. URL browser history, logs ya shared links mein aa sakta hai.


# 3. HTTP Request aur Response

# Jab tum website kholte ho, browser sirf ek request nahi bhejta. HTML ke alawa CSS, JavaScript, images aur APIs ke liye bhi alag requests ho sakti hain.

# Example: Request

# GET /profile HTTP/1.1
# Host: example.com
# Accept: text/html
# Cookie: session_id=REDACTED


# - GET: Resource maangne ka HTTP method.
# - /profile: Requested path.
# - Host: Requested domain.
# - Accept: Client kis type ka response accept kar sakta hai.
# - Cookie: Browser ke paas pehle se maujood cookie data, agar applicable ho.

# Example: Response

# HTTP/1.1 200 OK
# Content-Type: text/html
# Cache-Control: no-store


# - 200 OK: Request successful hui.
# - Content-Type: Response mein kis type ka content hai.
# - Cache-Control: no-store: Browser ya intermediary ko response store na karne ki instruction deta hai.
# Common status codes: 200 success, 301/302 redirect, 403 forbidden, 404 not found, 500 server error.



# 4. Headers kya hote hain?

# Headers request aur response ke saath extra information carry karte hain.

# Header	               Purpose

# Content-Type	            Response ka format batata hai
# Authorization	            Authentication credentials/token bhejne ke liye
# Cookie	                Browser se cookie data server tak bhejta hai
# Set-Cookie	            Server browser ko cookie set karne ka instruction deta hai
# Cache-Control	            Caching ke rules batata hai
# User-Agent	            Client software ke baare mein information deta hai
# Origin	                Cross-origin requests mein request ke origin ki information deta hai



# X- se shuru hone wale headers historically custom headers ke liye use hote the, lekin custom headers ka naam X- se shuru hona zaroori nahi hai.


# Security connection: Authorization ya Cookie jaise headers mein sensitive data ho sakta hai. Inhe screenshots, public logs ya GitHub par expose mat karna.



# 5. Cookies aur Sessions

# Cookie
# Browser mein store kiya gaya chhota data. Iska use login state, preferences aur tracking jaise purposes ke liye ho sakta hai.


# Session
# Server ya application ke through maintain ki gayi user interaction ki state. Traditional server-side sessions mein browser ek session ID cookie mein rakh sakta hai.



# Login ka example

# 1. Tum website par login karte ho.
# 2. Server login verify karta hai.
# 3. Server response mein Set-Cookie bhej sakta hai.
# 4. Browser cookie store karta hai.
# 5. Agli matching request mein browser Cookie header bhejta hai.
# 6. Server session ya token verify karke user ko access deta hai.

# Example response:
# Set-Cookie: session_id=REDACTED; Secure; HttpOnly; SameSite=Lax


# - Secure: Cookie sirf secure HTTPS connections par bheji jati hai.
# - HttpOnly: JavaScript se cookie read karna block karta hai.
# - SameSite=Lax: Kuch cross-site requests mein cookie bhejne ko restrict karta hai, lekin har CSRF scenario ka complete solution nahi hai.

# Important: Cookie aur session same cheez nahi hain. Cookie browser-side storage mechanism hai; session application ki state ko represent karta hai. Har website server-side sessions hi use kare, yeh zaroori nahi.


# 6. Browser caching

# Caching ka matlab hai kuch resources ko temporarily save karna, taaki agali baar unhe dobara download karne ki zaroorat kam ho.

# Cache behavior	    Meaning

# memory cache	        Resource browser ki memory se mila
# disk cache	        Resource local disk cache se mila
# 304 Not Modified	    Server ne bataya ki cached resource abhi valid hai
# 200 OK	            Request successful; resource response mein diya ja sakta hai


# Dhyan rahe: 200 OK ka matlab hamesha fresh download nahi hota. Browser cache se bhi response de sakta hai. Isi tarah 304 mein aam taur par resource ka naya body nahi bheja jata.


# 7. Practical Lab — Chrome DevTools

# Ab real practice karte hain. Kisi aisi website ka use karo jahan tumhara account login nahi hai, ya koi public website use karo.



# Practice 1: URL breakdown

# Chrome mein website open karo. Address bar se URL copy karke uske ye parts identify karo:
# - Protocol
# - Domain
# - Path
# - Query string, agar hai
# - Fragment, agar hai




# Practice 2: Set-Cookie header check karo

# Steps

# 1. Website open karo aur F12 dabao.
# 2. Network tab select karo.
# 3. Page reload karo.
# 4. Requests mein main document select karo — aam taur par Type document hota hai.
# 5. Headers → Response Headers mein Set-Cookie search karo.

# Note: Har website ya har page load par Set-Cookie dikhna zaroori nahi hai. Cookie set na ho toh result mein “Not observed” likh sakte ho.

# Cookie values ko copy ya share mat karna. Session cookies login access de sakti hain.



# Practice 3: Cache observe karo

# 1. Network tab khula rakho aur page reload karo.
# 2. Size ya Transferred column dekho.
# 3. Ab page ko dobara reload karo.
# 4. Dekho kaun-se resources memory cache, disk cache ya 304 dikhate hain.
# 5. DevTools ke Disable cache option ko sirf comparison ke liye try kar sakte ho. Yeh tabhi apply hota hai jab DevTools khula ho.

# Agar cache behavior clear nahi dikhta, koi CSS ya image-heavy public website try karo.