# शुभ विवाह डिजिटल निमन्त्रणा पत्र (Digital Wedding Invitation)
### विकल दाहाल & श्रद्धा दुलाल (Bikal Dahal & Shraddha Dulal)

A luxury animated digital wedding invitation card web application and high-resolution shareable digital image cards crafted specifically for social messaging apps (WhatsApp, Facebook Messenger, Instagram, Viber, Telegram).

---

## 📁 File Structure

- **`index.html`**: The interactive animated wedding invitation web application.
- **`style.css`**: Royal crimson & gold styling, 3D envelope fold animations, responsive layout.
- **`script.js`**: Procedural Web Audio API Mangal Dhun / Shehnai synthesizer, canvas falling flower petals (marigold & rose), live countdown timer, bilingual switcher, WhatsApp share utility, and photo gallery.
- **`invitation_card.png`**: High-resolution (1200 x 1800 px) digital invitation card ready to send directly as an image attachment in WhatsApp/Messenger.
- **`invitation_story.png`**: Vertical 9:16 format (1080 x 1920 px) tailored for WhatsApp Status, Facebook Stories, and Instagram Stories.
- **`generate_cards.py`**: Python script used to render high-resolution cards with Devanagari typography and photo framing.
- **`assets/`**: Standardized couple portraits, extracted calligraphy, and Ganesha/Kalash motifs.

---

## 🌟 Key Features

1. **Interactive 3D Opening Envelope**:
   - Realistic 3D royal envelope with gold wax seal stamped **"B & S"**.
   - Tapping the wax seal triggers a golden sparkle burst, flips open the envelope flap, slides up the invitation, and starts celebratory Mangal Dhun music!
2. **Falling Flower Petals (Canvas Physics)**:
   - Gentle marigold (*Sayapatri*) and rose petals fluttering softly down the screen.
3. **Procedural Shehnai / Mangal Dhun (Web Audio API)**:
   - Built-in classical Mangal Dhun melody with warm Tanpura drone that plays natively in any mobile or desktop browser without requiring any external audio files. Includes floating mute/play toggle.
4. **Couple Spotlight & Love Knot**:
   - Golden arched portraits for Groom **विकल दाहाल** and Bride **श्रद्धा दुलाल** with family lineage and addresses.
   - Interactive Lightbox Gallery showcasing the bride's photos.
5. **Live Countdown Timer**:
   - Real-time countdown to **२०८३ मंसिर १० (November 26, 2026, 08:00 AM)**.
6. **Ceremonial Schedule (वैवाहिक कार्यक्रम)**:
   - **जन्ति प्रस्थान**: २०८३ मंसिर १० गते बिहीबार | बिहान ८:०० बजे | पथरी शनिश्चरे -> बराहक्षेत्र-२, सुनसरी
   - **शुभ विवाह (दिवा लग्न)**: २०८३ मंसिर १० गते बिहीबार
   - **प्रीतिभोज**: २०८३ मंसिर ११ गते शुक्रबार | दिनको १:०० बजेदेखि | निजी निवास, पथरी शनिश्चरे-२, मोरङ
   - Interactive buttons for **Google Maps** turn-by-turn navigation and **Add to Google Calendar**.
7. **Direct Family Contact & WhatsApp RSVP**:
   - Direct call buttons to family contact numbers: `9842096841`, `9862325523`, `9840036925`.
   - 1-click **RSVP via WhatsApp** with pre-filled congratulatory response.
8. **Bilingual Toggle (नेपाली / English)**:
   - Seamless switch between traditional Nepali phrasing and English translation.

---

## 🚀 How to View Locally

Simply open `index.html` in any web browser, or launch a quick local server:

```bash
# Using Python
python3 -m http.server 8000
```
Then visit `http://localhost:8000` in your browser.

---

## 🌐 How to Host Online (Free Shareable Link)

To get a permanent link to share on WhatsApp and Messenger:

### Option 1: GitHub Pages (Recommended, 100% Free)
1. Push this folder to a GitHub repository.
2. In the repository settings, go to **Pages** -> Select `main` branch -> Click **Save**.
3. Your wedding invitation link will be live at: `https://<username>.github.io/<repo-name>/`.

### Option 2: Netlify / Vercel
- Drag and drop this folder directly onto [Netlify Drop](https://app.netlify.com/drop) to get an instant live HTTPS link in 10 seconds!

---

## 📲 How to Share via Messaging Apps (WhatsApp, Messenger, Viber)

1. **Option A (Web Link)**:
   - Share the hosted URL. When sent on WhatsApp, it automatically displays an auspicious preview with the couple's card and title.
   - Recipients can tap the wax seal, listen to the Shehnai music, see the countdown, view photos, and get map directions!
2. **Option B (Direct Image Attachment)**:
   - Directly send `invitation_card.png` in chats or post `invitation_story.png` on WhatsApp Status / Facebook Story!
