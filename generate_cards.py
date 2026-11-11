#!/usr/bin/env python3
"""
High-Resolution Digital Wedding Invitation Card Generator
For Bikal Dahal & Shraddha Dulal
Generates:
1. invitation_card.png (1200 x 1800 px, Portrait Master Card)
2. invitation_story.png (1080 x 1920 px, Vertical WhatsApp/Instagram Story)
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_BOLD = "/usr/share/fonts/truetype/noto/NotoSerifDevanagari-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf"
FONT_MED = "/usr/share/fonts/truetype/noto/NotoSerifDevanagari-Medium.ttf"

COLOR_BG_DEEP = (50, 4, 10)         # Deepest royal maroon
COLOR_BG_LIGHT = (110, 14, 28)      # Rich imperial crimson
COLOR_GOLD_LIGHT = (255, 235, 165)  # Highlight gold
COLOR_GOLD = (235, 190, 85)         # Classic gold
COLOR_GOLD_DARK = (175, 130, 40)    # Shadow gold
COLOR_CREAM = (255, 248, 235)       # Ivory cream
COLOR_WHITE = (255, 255, 255)

def draw_radial_background(width, height):
    """Create a rich radial gradient background with subtle gold dust vignette."""
    base = Image.new("RGB", (width, height), COLOR_BG_DEEP)
    draw = ImageDraw.Draw(base)
    cx, cy = width / 2.0, height * 0.42
    max_r = math.sqrt(cx**2 + cy**2) * 1.15
    
    steps = 100
    for i in range(steps, 0, -1):
        factor = i / steps
        r = max_r * factor
        red = int(COLOR_BG_LIGHT[0] * (1 - factor*0.55) + COLOR_BG_DEEP[0] * (factor*0.55))
        green = int(COLOR_BG_LIGHT[1] * (1 - factor*0.65) + COLOR_BG_DEEP[1] * (factor*0.65))
        blue = int(COLOR_BG_LIGHT[2] * (1 - factor*0.65) + COLOR_BG_DEEP[2] * (factor*0.65))
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(red, green, blue))
        
    return base.filter(ImageFilter.GaussianBlur(15))

def draw_ornate_borders(draw, width, height, inset=35):
    """Draw royal double gold borders with ornate corner motifs."""
    draw.rectangle([inset, inset, width - inset, height - inset], outline=COLOR_GOLD_DARK, width=2)
    inner_inset = inset + 12
    draw.rectangle([inner_inset, inner_inset, width - inner_inset, height - inner_inset], outline=COLOR_GOLD, width=4)
    third_inset = inner_inset + 8
    draw.rectangle([third_inset, third_inset, width - third_inset, height - third_inset], outline=COLOR_GOLD_LIGHT, width=1)
    
    corners = [
        (inner_inset, inner_inset, 1, 1),
        (width - inner_inset, inner_inset, -1, 1),
        (inner_inset, height - inner_inset, 1, -1),
        (width - inner_inset, height - inner_inset, -1, -1)
    ]
    for cx, cy, dx, dy in corners:
        for offset in range(5, 50, 6):
            draw.line([cx, cy + dy*offset, cx + dx*offset, cy], fill=COLOR_GOLD_LIGHT, width=2)
        draw.ellipse([cx + dx*20 - 6, cy + dy*20 - 6, cx + dx*20 + 6, cy + dy*20 + 6], fill=COLOR_GOLD)

def create_circular_framed_photo(img_path, size, border_width=10):
    """Crop photo into an elegant circle with triple gold border and glow."""
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    min_dim = min(w, h)
    left = (w - min_dim) // 2
    top = (h - min_dim) // 2
    img_cropped = img.crop((left, top, left + min_dim, top + min_dim)).resize((size, size), Image.Resampling.LANCZOS)
    
    mask = Image.new("L", (size, size), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse([border_width, border_width, size - border_width, size - border_width], fill=255)
    
    output = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    output.paste(img_cropped, (0, 0), mask)
    
    draw_out = ImageDraw.Draw(output)
    draw_out.ellipse([0, 0, size - 1, size - 1], outline=COLOR_GOLD_DARK, width=border_width)
    draw_out.ellipse([border_width//2, border_width//2, size - 1 - border_width//2, size - 1 - border_width//2], outline=COLOR_GOLD_LIGHT, width=3)
    draw_out.ellipse([border_width, border_width, size - 1 - border_width, size - 1 - border_width], outline=COLOR_GOLD, width=2)
    
    return output

def generate_invitation_card():
    width, height = 1200, 1800
    canvas = draw_radial_background(width, height)
    draw = ImageDraw.Draw(canvas)
    draw_ornate_borders(draw, width, height, inset=42)
    
    font_ganesha_title = ImageFont.truetype(FONT_BOLD, 32)
    font_shloka = ImageFont.truetype(FONT_REG, 23)
    font_couple_role = ImageFont.truetype(FONT_BOLD, 26)
    font_couple_names = ImageFont.truetype(FONT_BOLD, 48)
    font_couple_sub = ImageFont.truetype(FONT_MED, 23)
    font_couple_addr = ImageFont.truetype(FONT_BOLD, 23)
    font_invitation = ImageFont.truetype(FONT_REG, 24)
    font_event_hdr = ImageFont.truetype(FONT_BOLD, 30)
    font_event_body = ImageFont.truetype(FONT_BOLD, 24)
    font_event_sub = ImageFont.truetype(FONT_REG, 22)
    font_family_hdr = ImageFont.truetype(FONT_BOLD, 24)
    font_family_body = ImageFont.truetype(FONT_REG, 19)
    font_family_sub = ImageFont.truetype(FONT_BOLD, 19)
    font_contact = ImageFont.truetype(FONT_BOLD, 24)
    
    y = 65
    
    # 1. Ganesha icon
    if os.path.exists("assets/ganesha_gold.png"):
        g_img = Image.open("assets/ganesha_gold.png")
        gw = 65
        gh = int(g_img.height * (gw / g_img.width))
        g_res = g_img.resize((gw, gh), Image.Resampling.LANCZOS)
        canvas.paste(g_res, ((width - gw)//2, y), g_res)
        y += gh + 12
        
    text_ganesha = "॥ श्री गणेशाय नम: ॥"
    bbox = font_ganesha_title.getbbox(text_ganesha)
    draw.text(((width - (bbox[2] - bbox[0]))/2, y), text_ganesha, font=font_ganesha_title, fill=COLOR_GOLD_LIGHT)
    y += 46
    
    s1 = "मंगलम् भगवान् विष्णुः मङ्गलम् गरुडध्वजः ।"
    s2 = "मङ्गलम् पुण्डरीकाक्षः मङ्गलाय तनो हरी ॥"
    bbox1 = font_shloka.getbbox(s1)
    bbox2 = font_shloka.getbbox(s2)
    draw.text(((width - (bbox1[2] - bbox1[0]))/2, y), s1, font=font_shloka, fill=COLOR_GOLD)
    y += 32
    draw.text(((width - (bbox2[2] - bbox2[0]))/2, y), s2, font=font_shloka, fill=COLOR_GOLD)
    y += 40
    
    # 2. शुभ विवाह Calligraphy
    if os.path.exists("assets/shubha_vivaha_gold.png"):
        sv_img = Image.open("assets/shubha_vivaha_gold.png")
        sv_w = 460
        sv_h = int(sv_img.height * (sv_w / sv_img.width))
        sv_resized = sv_img.resize((sv_w, sv_h), Image.Resampling.LANCZOS)
        canvas.paste(sv_resized, ((width - sv_w)//2, y), sv_resized)
        y += sv_h + 30
    
    # 3. Couple Section
    photo_size = 310
    frame_y = y
    gx = 140
    bx = width - 140 - photo_size
    
    # Groom Photo
    groom_path = "assets/groom_royal.jpg" if os.path.exists("assets/groom_royal.jpg") else "assets/groom.jpg"
    groom_photo = create_circular_framed_photo(groom_path, photo_size)
    canvas.paste(groom_photo, (gx, frame_y), groom_photo)
    
    # Bride Photo
    bride_photo = create_circular_framed_photo("assets/bride_portrait.jpg" if os.path.exists("assets/bride_portrait.jpg") else "assets/bride.jpg", photo_size)
    canvas.paste(bride_photo, (bx, frame_y), bride_photo)
    
    # Center Kalash
    if os.path.exists("assets/kalash_gold.png"):
        k_img = Image.open("assets/kalash_gold.png")
        kw = 95
        kh = int(k_img.height * (kw / k_img.width))
        k_res = k_img.resize((kw, kh), Image.Resampling.LANCZOS)
        canvas.paste(k_res, ((width - kw)//2, frame_y + (photo_size - kh)//2 - 25), k_res)
    
    text_weds = "परिणय"
    w_bbox = font_couple_role.getbbox(text_weds)
    draw.text(((width - (w_bbox[2] - w_bbox[0]))/2, frame_y + photo_size//2 + 50), text_weds, font=font_couple_role, fill=COLOR_GOLD_LIGHT)
    
    # Groom Details
    gy = frame_y + photo_size + 18
    g_title = "॥ दुल्हा ॥"
    draw.text((gx + photo_size/2 - font_couple_role.getbbox(g_title)[2]/2, gy), g_title, font=font_couple_role, fill=COLOR_GOLD_LIGHT)
    gy += 38
    g_name = "विकल दाहाल"
    draw.text((gx + photo_size/2 - font_couple_names.getbbox(g_name)[2]/2, gy), g_name, font=font_couple_names, fill=COLOR_WHITE)
    gy += 60
    g_p1 = "चिरञ्जीवी सुपुत्र:"
    draw.text((gx + photo_size/2 - font_couple_sub.getbbox(g_p1)[2]/2, gy), g_p1, font=font_couple_sub, fill=COLOR_GOLD)
    gy += 30
    g_p2 = "खेमनाथ दाहाल र भिमकुमारी दाहाल"
    draw.text((gx + photo_size/2 - font_couple_sub.getbbox(g_p2)[2]/2, gy), g_p2, font=font_couple_sub, fill=COLOR_CREAM)
    gy += 30
    g_addr = "पथरी शनिश्चरे-२, मोरङ"
    draw.text((gx + photo_size/2 - font_couple_addr.getbbox(g_addr)[2]/2, gy), g_addr, font=font_couple_addr, fill=COLOR_GOLD_LIGHT)
    
    # Bride Details
    by = frame_y + photo_size + 18
    b_title = "॥ दुल्ही ॥"
    draw.text((bx + photo_size/2 - font_couple_role.getbbox(b_title)[2]/2, by), b_title, font=font_couple_role, fill=COLOR_GOLD_LIGHT)
    by += 38
    b_name = "श्रद्धा दुलाल"
    draw.text((bx + photo_size/2 - font_couple_names.getbbox(b_name)[2]/2, by), b_name, font=font_couple_names, fill=COLOR_WHITE)
    by += 60
    b_p1 = "आयुष्मती सुपुत्री:"
    draw.text((bx + photo_size/2 - font_couple_sub.getbbox(b_p1)[2]/2, by), b_p1, font=font_couple_sub, fill=COLOR_GOLD)
    by += 30
    b_p2 = "प्रकाश दुलाल र शान्ता दुलाल"
    draw.text((bx + photo_size/2 - font_couple_sub.getbbox(b_p2)[2]/2, by), b_p2, font=font_couple_sub, fill=COLOR_CREAM)
    by += 30
    b_addr = "बराहक्षेत्र-२, उदयचोक, सुनसरी"
    draw.text((bx + photo_size/2 - font_couple_addr.getbbox(b_addr)[2]/2, by), b_addr, font=font_couple_addr, fill=COLOR_GOLD_LIGHT)
    
    # 4. Formal Invitation Paragraph
    y = max(gy, by) + 42
    inv_line1 = "यही मिति २०८३ साल मंसिर १० गते बिहीबारका दिन दिवा लग्नको शुभ-विवाह सु-सम्पन्न हुने निश्चय भएको हुँदा"
    inv_line2 = "उक्त शुभ अवसरमा उपस्थित भई नव वर-वधुलाई शुभ आशिर्वाद प्रदान गरिदिनुहुन"
    inv_line3 = "यहाँहरुको गरिमामय उपस्थितिको लागि हार्दिक सादर निमन्त्रणा गर्दछौं ।"
    
    for line in [inv_line1, inv_line2, inv_line3]:
        bbox = font_invitation.getbbox(line)
        draw.text(((width - (bbox[2] - bbox[0]))/2, y), line, font=font_invitation, fill=COLOR_CREAM)
        y += 34
        
    y += 20
    
    # 5. Event Schedule Highlight Cards
    card_w = (width - 150) // 2
    card_h = 220
    card1_x = 65
    card2_x = width - 65 - card_w
    
    # Card 1: जन्ति प्रस्थान
    draw.rounded_rectangle([card1_x, y, card1_x + card_w, y + card_h], radius=16, fill=(45, 4, 10), outline=COLOR_GOLD, width=2)
    draw.rounded_rectangle([card1_x, y, card1_x + card_w, y + 50], radius=14, fill=(115, 16, 30))
    ev1_title = "॥ जन्ति प्रस्थान एवं शुभ-विवाह ॥"
    draw.text((card1_x + (card_w - font_event_hdr.getbbox(ev1_title)[2])/2, y + 10), ev1_title, font=font_event_hdr, fill=COLOR_GOLD_LIGHT)
    
    draw.text((card1_x + 25, y + 66), "मिति : २०८३ मंसिर १० गते (बिहीबार)", font=font_event_body, fill=COLOR_WHITE)
    draw.text((card1_x + 25, y + 102), "समय : बिहान ८:०० बजे प्रस्थान", font=font_event_body, fill=COLOR_GOLD_LIGHT)
    draw.text((card1_x + 25, y + 138), "स्थान : बराहक्षेत्र-२, उदयचोक, सुनसरी", font=font_event_sub, fill=COLOR_CREAM)
    draw.text((card1_x + 25, y + 172), "लग्न : दिवा लग्नको शुभ-विवाह", font=font_event_sub, fill=COLOR_GOLD)
    
    # Card 2: प्रीतिभोज
    draw.rounded_rectangle([card2_x, y, card2_x + card_w, y + card_h], radius=16, fill=(45, 4, 10), outline=COLOR_GOLD, width=2)
    draw.rounded_rectangle([card2_x, y, card2_x + card_w, y + 50], radius=14, fill=(115, 16, 30))
    ev2_title = "॥ प्रीतिभोज (भोज) ॥"
    draw.text((card2_x + (card_w - font_event_hdr.getbbox(ev2_title)[2])/2, y + 10), ev2_title, font=font_event_hdr, fill=COLOR_GOLD_LIGHT)
    
    draw.text((card2_x + 25, y + 66), "मिति : २०८३ मंसिर ११ गते (शुक्रबार)", font=font_event_body, fill=COLOR_WHITE)
    draw.text((card2_x + 25, y + 102), "समय : दिनको १:०० बजेदेखि", font=font_event_body, fill=COLOR_GOLD_LIGHT)
    draw.text((card2_x + 25, y + 138), "स्थान : निजी निवास", font=font_event_body, fill=COLOR_CREAM)
    draw.text((card2_x + 25, y + 172), "पथरी शनिश्चरे न.पा.-२, मोरङ", font=font_event_sub, fill=COLOR_GOLD)
    
    y += card_h + 35
    
    # 6. Family & RSVP Footer Section
    draw.line([80, y, width - 80, y], fill=COLOR_GOLD_DARK, width=2)
    y += 22
    
    col1_x = 80
    col2_x = 450
    col3_x = 830
    
    # Col 1: प्रार्थी & सम्झना
    draw.text((col1_x, y), "॥ प्रार्थी ॥", font=font_family_hdr, fill=COLOR_GOLD_LIGHT)
    draw.text((col1_x, y + 32), "हजुरआमा : डिकुरादेवी दाहाल, टंकादेवी दाहाल", font=font_family_body, fill=COLOR_CREAM)
    draw.text((col1_x, y + 60), "बुवा : खेमनाथ दाहाल", font=font_family_body, fill=COLOR_CREAM)
    draw.text((col1_x, y + 86), "आमा : भिमकुमारी दाहाल", font=font_family_body, fill=COLOR_CREAM)
    draw.text((col1_x, y + 116), "॥ सम्झनामा ॥ स्व. होमनाथ दाहाल, स्व. भोजराज भण्डारी", font=font_family_sub, fill=COLOR_GOLD)
    
    # Col 2: दर्शनाभिलाषी
    draw.text((col2_x, y), "॥ दर्शनाभिलाषी ॥", font=font_family_hdr, fill=COLOR_GOLD_LIGHT)
    draw.text((col2_x, y + 32), "काका-काकी, फुपु-फुपाजु, मामा-माइजु", font=font_family_body, fill=COLOR_CREAM)
    draw.text((col2_x, y + 60), "हजुरआमा : रुक्मिणा भण्डारी", font=font_family_body, fill=COLOR_CREAM)
    draw.text((col2_x, y + 86), "भाइहरू : पशुपतिनाथ, युदिन, युसुफ दाहाल", font=font_family_body, fill=COLOR_CREAM)
    draw.text((col2_x, y + 116), "एवम् समस्त दाहाल परिवार", font=font_family_sub, fill=COLOR_GOLD)
    
    # Col 3: सम्पर्क
    draw.text((col3_x, y), "॥ सम्पर्क / निमन्त्रणा ॥", font=font_family_hdr, fill=COLOR_GOLD_LIGHT)
    draw.text((col3_x, y + 34), "फोन : ९८४२०९६८४१", font=font_contact, fill=COLOR_WHITE)
    draw.text((col3_x, y + 68), "फोन : ९८६२३२५५२३", font=font_contact, fill=COLOR_WHITE)
    draw.text((col3_x, y + 102), "फोन : ९८४००३६९२५", font=font_contact, fill=COLOR_WHITE)
    
    out_path = "invitation_card.png"
    canvas.save(out_path, quality=95)
    print("Successfully generated", out_path)

def generate_invitation_story():
    """Generate 1080 x 1920 vertical format for WhatsApp Status & Stories."""
    width, height = 1080, 1920
    canvas = draw_radial_background(width, height)
    draw = ImageDraw.Draw(canvas)
    draw_ornate_borders(draw, width, height, inset=35)
    
    font_ganesha = ImageFont.truetype(FONT_BOLD, 30)
    font_shloka = ImageFont.truetype(FONT_REG, 21)
    font_names = ImageFont.truetype(FONT_BOLD, 46)
    font_titles = ImageFont.truetype(FONT_BOLD, 26)
    font_details = ImageFont.truetype(FONT_MED, 22)
    font_event_hdr = ImageFont.truetype(FONT_BOLD, 30)
    font_event_body = ImageFont.truetype(FONT_BOLD, 24)
    font_event_sub = ImageFont.truetype(FONT_REG, 21)
    font_family = ImageFont.truetype(FONT_REG, 21)
    font_rsvp = ImageFont.truetype(FONT_BOLD, 24)
    
    y = 65
    
    if os.path.exists("assets/ganesha_gold.png"):
        g_img = Image.open("assets/ganesha_gold.png")
        gw = 65
        gh = int(g_img.height * (gw / g_img.width))
        g_res = g_img.resize((gw, gh), Image.Resampling.LANCZOS)
        canvas.paste(g_res, ((width - gw)//2, y), g_res)
        y += gh + 12
        
    text_ganesha = "॥ श्री गणेशाय नम: ॥"
    bbox = font_ganesha.getbbox(text_ganesha)
    draw.text(((width - (bbox[2] - bbox[0]))/2, y), text_ganesha, font=font_ganesha, fill=COLOR_GOLD_LIGHT)
    y += 44
    
    s1 = "मंगलम् भगवान् विष्णुः मङ्गलम् गरुडध्वजः ।"
    s2 = "मङ्गलम् पुण्डरीकाक्षः मङ्गलाय तनो हरी ॥"
    bbox1 = font_shloka.getbbox(s1)
    bbox2 = font_shloka.getbbox(s2)
    draw.text(((width - (bbox1[2] - bbox1[0]))/2, y), s1, font=font_shloka, fill=COLOR_GOLD)
    y += 30
    draw.text(((width - (bbox2[2] - bbox2[0]))/2, y), s2, font=font_shloka, fill=COLOR_GOLD)
    y += 38
    
    if os.path.exists("assets/shubha_vivaha_gold.png"):
        sv_img = Image.open("assets/shubha_vivaha_gold.png")
        sv_w = 420
        sv_h = int(sv_img.height * (sv_w / sv_img.width))
        sv_resized = sv_img.resize((sv_w, sv_h), Image.Resampling.LANCZOS)
        canvas.paste(sv_resized, ((width - sv_w)//2, y), sv_resized)
        y += sv_h + 30
    
    photo_size = 280
    frame_y = y
    gx = 130
    bx = width - 130 - photo_size
    
    groom_path = "assets/groom_royal.jpg" if os.path.exists("assets/groom_royal.jpg") else "assets/groom.jpg"
    groom_photo = create_circular_framed_photo(groom_path, photo_size)
    canvas.paste(groom_photo, (gx, frame_y), groom_photo)
    
    bride_photo = create_circular_framed_photo("assets/bride_portrait.jpg" if os.path.exists("assets/bride_portrait.jpg") else "assets/bride.jpg", photo_size)
    canvas.paste(bride_photo, (bx, frame_y), bride_photo)
    
    text_weds = "परिणय"
    w_bbox = font_titles.getbbox(text_weds)
    draw.text(((width - (w_bbox[2] - w_bbox[0]))/2, frame_y + photo_size//2 - 15), text_weds, font=font_titles, fill=COLOR_GOLD_LIGHT)
    
    # Groom details
    gy = frame_y + photo_size + 18
    g_title = "॥ वर (दुल्हा) ॥"
    draw.text((gx + photo_size/2 - font_titles.getbbox(g_title)[2]/2, gy), g_title, font=font_titles, fill=COLOR_GOLD_LIGHT)
    gy += 36
    g_name = "विकल दाहाल"
    draw.text((gx + photo_size/2 - font_names.getbbox(g_name)[2]/2, gy), g_name, font=font_names, fill=COLOR_WHITE)
    gy += 55
    g_p = "सुपुत्र: खेमनाथ र भिमकुमारी दाहाल"
    draw.text((gx + photo_size/2 - font_details.getbbox(g_p)[2]/2, gy), g_p, font=font_details, fill=COLOR_CREAM)
    gy += 28
    g_a = "पथरी शनिश्चरे-२, मोरङ"
    draw.text((gx + photo_size/2 - font_details.getbbox(g_a)[2]/2, gy), g_a, font=font_details, fill=COLOR_GOLD)
    
    # Bride details
    by = frame_y + photo_size + 18
    b_title = "॥ वधु (दुल्ही) ॥"
    draw.text((bx + photo_size/2 - font_titles.getbbox(b_title)[2]/2, by), b_title, font=font_titles, fill=COLOR_GOLD_LIGHT)
    by += 36
    b_name = "श्रद्धा दुलाल"
    draw.text((bx + photo_size/2 - font_names.getbbox(b_name)[2]/2, by), b_name, font=font_names, fill=COLOR_WHITE)
    by += 55
    b_p = "सुपुत्री: प्रकाश र शान्ता दुलाल"
    draw.text((bx + photo_size/2 - font_details.getbbox(b_p)[2]/2, by), b_p, font=font_details, fill=COLOR_CREAM)
    by += 28
    b_a = "बराहक्षेत्र-२, उदयचोक, सुनसरी"
    draw.text((bx + photo_size/2 - font_details.getbbox(b_a)[2]/2, by), b_a, font=font_details, fill=COLOR_GOLD)
    
    y = max(gy, by) + 45
    
    note = "नव वर-वधुलाई शुभ आशिर्वाद दिन यहाँहरुको हार्दिक निमन्त्रणा छ"
    bbox = font_titles.getbbox(note)
    draw.text(((width - (bbox[2] - bbox[0]))/2, y), note, font=font_titles, fill=COLOR_CREAM)
    y += 50
    
    # Event 1: जन्ति प्रस्थान
    b_w = width - 140
    b_x = 70
    draw.rounded_rectangle([b_x, y, b_x + b_w, y + 175], radius=16, fill=(45, 4, 10), outline=COLOR_GOLD, width=2)
    draw.text((b_x + 25, y + 18), "॥ जन्ति प्रस्थान एवं दिवा लग्न शुभ-विवाह ॥", font=font_event_hdr, fill=COLOR_GOLD_LIGHT)
    draw.text((b_x + 25, y + 62), "मिति : २०८३ मंसिर १० गते बिहीबार | बिहान ८:०० बजे", font=font_event_body, fill=COLOR_WHITE)
    draw.text((b_x + 25, y + 100), "स्थान : निजी निवास (पथरी) बाट बराहक्षेत्र-२, सुनसरी", font=font_event_sub, fill=COLOR_CREAM)
    draw.text((b_x + 25, y + 132), "लग्न : दिवा लग्नको वैदिक विवाह संस्कार सम्पन्न हुनेछ", font=font_event_sub, fill=COLOR_GOLD)
    y += 205
    
    # Event 2: प्रीतिभोज
    draw.rounded_rectangle([b_x, y, b_x + b_w, y + 175], radius=16, fill=(45, 4, 10), outline=COLOR_GOLD, width=2)
    draw.text((b_x + 25, y + 18), "॥ प्रीतिभोज (भोज) ॥", font=font_event_hdr, fill=COLOR_GOLD_LIGHT)
    draw.text((b_x + 25, y + 62), "मिति : २०८३ मंसिर ११ गते शुक्रबार | दिनको १:०० बजेदेखि", font=font_event_body, fill=COLOR_WHITE)
    draw.text((b_x + 25, y + 100), "स्थान : निजी निवास, पथरी शनिश्चरे न.पा.-२, मोरङ", font=font_event_body, fill=COLOR_CREAM)
    draw.text((b_x + 25, y + 132), "यहाँहरूको गरिमामय उपस्थितिको हार्दिक अपेक्षा गर्दछौं", font=font_event_sub, fill=COLOR_GOLD)
    y += 205
    
    draw.text((b_x + 20, y), "प्रार्थी: खेमनाथ / भिमकुमारी दाहाल | दर्शनाभिलाषी: समस्त दाहाल परिवार", font=font_family, fill=COLOR_GOLD)
    y += 45
    
    # RSVP Box
    draw.rounded_rectangle([b_x, y, b_x + b_w, y + 80], radius=12, fill=(115, 16, 30), outline=COLOR_GOLD_LIGHT, width=2)
    rsvp_txt = "सम्पर्क नम्बर : ९८४२०९६८४१, ९८६२३२५५२३, ९८४००३६९२५"
    r_bbox = font_rsvp.getbbox(rsvp_txt)
    draw.text(((width - (r_bbox[2] - r_bbox[0]))/2, y + 25), rsvp_txt, font=font_rsvp, fill=COLOR_WHITE)
    
    out_path = "invitation_story.png"
    canvas.save(out_path, quality=95)
    print("Successfully generated", out_path)

if __name__ == "__main__":
    generate_invitation_card()
    generate_invitation_story()
