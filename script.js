/**
 * ROYAL WEDDING INVITATION INTERACTIVE ENGINE
 * For Bikal Dahal & Shraddha Dulal
 * Features:
 * - Procedural Web Audio Mangal Dhun / Shehnai Synthesizer
 * - Canvas Falling Rose & Marigold Petal Particle System
 * - 3D Envelope Opening & Wax Seal Burst
 * - Live Countdown to Mansir 10, 2083 (26 Nov 2026, 08:00 AM)
 * - Bilingual Switcher (Nepali / English)
 * - WhatsApp Share & Instant Copy Utility
 * - Google Calendar Integration
 * - Bride Photo Gallery Lightbox
 */

document.addEventListener('DOMContentLoaded', () => {
  initPetalCanvas();
  initEnvelopeOpening();
  initCountdownTimer();
  initAudioSynthesizer();
  initLanguageToggle();
  initSocialSharing();
  initGalleryModal();
  initOriginalCardModal();
});

/* =========================================================
   1. CANVAS FALLING FLOWER PETALS (Rose & Marigold)
   ========================================================= */
function initPetalCanvas() {
  const canvas = document.getElementById('petalsCanvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let width = (canvas.width = window.innerWidth);
  let height = (canvas.height = window.innerHeight);

  window.addEventListener('resize', () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  });

  const petals = [];
  const maxPetals = window.innerWidth < 600 ? 30 : 55;

  const colors = [
    { type: 'marigold', r: 255, g: 153, b: 0 },    // Saffron Orange
    { type: 'marigold', r: 255, g: 190, b: 20 },   // Golden Yellow
    { type: 'rose', r: 196, g: 30, b: 58 },        // Crimson Red
    { type: 'rose', r: 155, g: 17, b: 30 }         // Deep Burgundy
  ];

  class Petal {
    constructor() {
      this.reset(true);
    }

    reset(initial = false) {
      this.x = Math.random() * width;
      this.y = initial ? Math.random() * height : -20;
      this.size = Math.random() * 9 + 8; // 8 - 17px
      this.speedY = Math.random() * 1.5 + 1.0;
      this.speedX = Math.random() * 1.2 - 0.6;
      this.angle = Math.random() * Math.PI * 2;
      this.angularSpeed = (Math.random() - 0.5) * 0.04;
      this.flip = Math.random() * Math.PI;
      this.flipSpeed = Math.random() * 0.03 + 0.01;
      this.color = colors[Math.floor(Math.random() * colors.length)];
      this.opacity = Math.random() * 0.35 + 0.55;
    }

    update() {
      this.y += this.speedY;
      this.x += Math.sin(this.angle) * 1.2 + this.speedX;
      this.angle += this.angularSpeed;
      this.flip += this.flipSpeed;

      if (this.y > height + 20 || this.x < -30 || this.x > width + 30) {
        this.reset();
      }
    }

    draw() {
      ctx.save();
      ctx.translate(this.x, this.y);
      ctx.rotate(this.angle);
      ctx.scale(1, Math.cos(this.flip));

      ctx.beginPath();
      // Draw organic petal curve
      if (this.color.type === 'marigold') {
        // Slightly elongated teardrop petal
        ctx.moveTo(0, -this.size);
        ctx.bezierCurveTo(this.size * 0.6, -this.size * 0.5, this.size * 0.7, this.size * 0.6, 0, this.size);
        ctx.bezierCurveTo(-this.size * 0.7, this.size * 0.6, -this.size * 0.6, -this.size * 0.5, 0, -this.size);
      } else {
        // Rounded velvety rose petal
        ctx.moveTo(0, -this.size * 0.8);
        ctx.bezierCurveTo(this.size * 0.8, -this.size * 0.8, this.size, this.size * 0.5, 0, this.size);
        ctx.bezierCurveTo(-this.size, this.size * 0.5, -this.size * 0.8, -this.size * 0.8, 0, -this.size * 0.8);
      }

      ctx.fillStyle = `rgba(${this.color.r}, ${this.color.g}, ${this.color.b}, ${this.opacity})`;
      ctx.shadowColor = `rgba(${this.color.r}, ${this.color.g}, ${this.color.b}, 0.3)`;
      ctx.shadowBlur = 4;
      ctx.fill();
      ctx.restore();
    }
  }

  for (let i = 0; i < maxPetals; i++) {
    petals.push(new Petal());
  }

  function render() {
    ctx.clearRect(0, 0, width, height);
    for (let i = 0; i < petals.length; i++) {
      petals[i].update();
      petals[i].draw();
    }
    requestAnimationFrame(render);
  }

  render();
}

/* =========================================================
   2. 3D ENVELOPE OPENING & WAX SEAL BURST
   ========================================================= */
function initEnvelopeOpening() {
  const overlay = document.getElementById('envelopeOverlay');
  const envelope = document.getElementById('envelope');
  const waxSeal = document.getElementById('waxSeal');
  const openCardBtn = document.getElementById('openCardBtn');

  function openEnvelope() {
    if (envelope.classList.contains('opening')) return;
    envelope.classList.add('opening');

    // Start celebratory Mangal Dhun
    startMangalDhunAudio();

    // Spawn burst confetti particles
    burstGoldSparkles(waxSeal.getBoundingClientRect());

    // Transition out overlay after flip animation completes
    setTimeout(() => {
      overlay.classList.add('opened');
      // Scroll smoothly to top of card
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }, 1100);
  }

  if (waxSeal) waxSeal.addEventListener('click', openEnvelope);
  if (openCardBtn) openCardBtn.addEventListener('click', openEnvelope);
  if (envelope) envelope.addEventListener('click', (e) => {
    // Only open if clicking body or seal
    if (!envelope.classList.contains('opening')) {
      openEnvelope();
    }
  });
}

function burstGoldSparkles(rect) {
  const count = 35;
  const cx = rect.left + rect.width / 2;
  const cy = rect.top + rect.height / 2;

  for (let i = 0; i < count; i++) {
    const el = document.createElement('div');
    el.style.position = 'fixed';
    el.style.left = `${cx}px`;
    el.style.top = `${cy}px`;
    el.style.width = `${Math.random() * 8 + 4}px`;
    el.style.height = el.style.width;
    el.style.backgroundColor = Math.random() > 0.5 ? '#ffd700' : '#ffea75';
    el.style.borderRadius = '50%';
    el.style.pointerEvents = 'none';
    el.style.zIndex = '10000';
    el.style.boxShadow = '0 0 10px #ffd700';

    document.body.appendChild(el);

    const angle = Math.random() * Math.PI * 2;
    const velocity = Math.random() * 140 + 60;
    const destX = Math.cos(angle) * velocity;
    const destY = Math.sin(angle) * velocity;

    el.animate([
      { transform: 'translate(0, 0) scale(1)', opacity: 1 },
      { transform: `translate(${destX}px, ${destY}px) scale(0)`, opacity: 0 }
    ], {
      duration: Math.random() * 600 + 600,
      easing: 'cubic-bezier(0.1, 0.9, 0.2, 1)'
    }).onfinish = () => el.remove();
  }
}

/* =========================================================
   3. WEB AUDIO API MANGAL DHUN / SHEHNAI SYNTHESIZER
   ========================================================= */
let audioCtx = null;
let isAudioPlaying = false;
let audioTimer = null;
let droneGain = null;

function initAudioSynthesizer() {
  const musicToggleBtn = document.getElementById('musicToggleBtn');
  if (!musicToggleBtn) return;

  musicToggleBtn.addEventListener('click', () => {
    if (!audioCtx) {
      startMangalDhunAudio();
    } else {
      if (isAudioPlaying) {
        pauseMangalDhun();
      } else {
        resumeMangalDhun();
      }
    }
  });
}

function startMangalDhunAudio() {
  try {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) return;
    
    if (!audioCtx) {
      audioCtx = new AudioContext();
    }

    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }

    startDrone();
    startShehnaiMelody();
    isAudioPlaying = true;
    updateMusicUI(true);
  } catch (err) {
    console.warn('Audio synthesis not supported or blocked:', err);
  }
}

function updateMusicUI(playing) {
  const musicToggleBtn = document.getElementById('musicToggleBtn');
  const musicIcon = document.getElementById('musicIcon');
  if (!musicToggleBtn) return;

  if (playing) {
    musicToggleBtn.classList.add('playing');
    if (musicIcon) musicIcon.textContent = '🎶';
  } else {
    musicToggleBtn.classList.remove('playing');
    if (musicIcon) musicIcon.textContent = '🔇';
  }
}

function pauseMangalDhun() {
  if (!audioCtx) return;
  if (droneGain) droneGain.gain.setTargetAtTime(0, audioCtx.currentTime, 0.1);
  if (audioTimer) clearTimeout(audioTimer);
  isAudioPlaying = false;
  updateMusicUI(false);
}

function resumeMangalDhun() {
  if (!audioCtx) return;
  if (audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
  if (droneGain) droneGain.gain.setTargetAtTime(0.08, audioCtx.currentTime, 0.1);
  startShehnaiMelody();
  isAudioPlaying = true;
  updateMusicUI(true);
}

// Warm Tanpura Sa-Pa Drone
function startDrone() {
  // Key of C# (138.59 Hz Sa, 207.65 Hz Pa)
  const masterGain = audioCtx.createGain();
  masterGain.gain.setValueAtTime(0.08, audioCtx.currentTime);
  masterGain.connect(audioCtx.destination);
  droneGain = masterGain;

  const frequencies = [138.59, 207.65, 277.18];
  frequencies.forEach(f => {
    const osc = audioCtx.createOscillator();
    osc.type = 'sawtooth';
    osc.frequency.setValueAtTime(f, audioCtx.currentTime);

    const filter = audioCtx.createBiquadFilter();
    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(450, audioCtx.currentTime);

    osc.connect(filter);
    filter.connect(masterGain);
    osc.start();
  });
}

// Classical Mangal Dhun Melody (Shehnai timbre with gentle vibrato)
function startShehnaiMelody() {
  // Auspicious Bilawal/Kalyan melodic notes for wedding celebrations
  // Sa (C#4: 277.18), Re (311.13), Ga (349.23), Ma (369.99), Pa (415.30), Dha (466.16), Ni (523.25), Sa' (554.37)
  const notes = [
    { f: 277.18, d: 0.5 }, // Sa
    { f: 311.13, d: 0.5 }, // Re
    { f: 349.23, d: 0.75 }, // Ga
    { f: 415.30, d: 0.5 }, // Pa
    { f: 466.16, d: 0.5 }, // Dha
    { f: 415.30, d: 0.75 }, // Pa
    { f: 554.37, d: 1.0 }, // Sa'
    { f: 523.25, d: 0.4 }, // Ni
    { f: 466.16, d: 0.4 }, // Dha
    { f: 415.30, d: 0.75 }, // Pa
    { f: 349.23, d: 0.5 }, // Ga
    { f: 311.13, d: 0.5 }, // Re
    { f: 277.18, d: 1.2 }, // Sa
    { f: 0, d: 0.4 }       // rest
  ];

  let noteIndex = 0;

  function playNextNote() {
    if (!isAudioPlaying) return;

    const note = notes[noteIndex];
    if (note.f > 0) {
      playShehnaiNote(note.f, note.d);
    }

    noteIndex = (noteIndex + 1) % notes.length;
    audioTimer = setTimeout(playNextNote, note.d * 900);
  }

  playNextNote();
}

function playShehnaiNote(freq, duration) {
  if (!audioCtx) return;
  const now = audioCtx.currentTime;

  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();

  // Vibrato (subtle frequency modulation typical of Shehnai)
  const vibrato = audioCtx.createOscillator();
  const vibratoGain = audioCtx.createGain();
  vibrato.frequency.setValueAtTime(5.5, now); // 5.5 Hz vibrato rate
  vibratoGain.gain.setValueAtTime(freq * 0.015, now); // vibrato depth
  vibrato.connect(osc.frequency);
  vibrato.start(now);

  osc.type = 'triangle';
  osc.frequency.setValueAtTime(freq, now);

  // Envelope
  gain.gain.setValueAtTime(0, now);
  gain.gain.linearRampToValueAtTime(0.12, now + 0.08); // soft attack
  gain.gain.exponentialRampToValueAtTime(0.001, now + duration);

  const filter = audioCtx.createBiquadFilter();
  filter.type = 'bandpass';
  filter.frequency.setValueAtTime(freq * 2.2, now);
  filter.Q.setValueAtTime(1.8, now);

  osc.connect(filter);
  filter.connect(gain);
  gain.connect(audioCtx.destination);

  osc.start(now);
  osc.stop(now + duration);
  vibrato.stop(now + duration);
}

/* =========================================================
   4. LIVE WEDDING COUNTDOWN TIMER
   ========================================================= */
function initCountdownTimer() {
  // Target: 2083 Mansir 10 at 08:00 AM (Gregorian: Nov 26, 2026, 08:00:00 GMT+0545 Nepal Time)
  const weddingDate = new Date('2026-11-26T08:00:00+05:45').getTime();

  const daysEl = document.getElementById('timerDays');
  const hoursEl = document.getElementById('timerHours');
  const minsEl = document.getElementById('timerMinutes');
  const secsEl = document.getElementById('timerSeconds');
  const celebrationMsg = document.getElementById('countdownCelebration');

  function update() {
    const now = new Date().getTime();
    const distance = weddingDate - now;

    if (distance <= 0) {
      if (daysEl) daysEl.textContent = '00';
      if (hoursEl) hoursEl.textContent = '00';
      if (minsEl) minsEl.textContent = '00';
      if (secsEl) secsEl.textContent = '00';
      if (celebrationMsg) celebrationMsg.style.display = 'block';
      return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    if (daysEl) daysEl.textContent = days < 10 ? '0' + days : days;
    if (hoursEl) hoursEl.textContent = hours < 10 ? '0' + hours : hours;
    if (minsEl) minsEl.textContent = minutes < 10 ? '0' + minutes : minutes;
    if (secsEl) secsEl.textContent = seconds < 10 ? '0' + seconds : seconds;
  }

  update();
  setInterval(update, 1000);
}

/* =========================================================
   5. BILINGUAL LANGUAGE SWITCHER (नेपाली / English)
   ========================================================= */
let currentLang = 'ne';

function initLanguageToggle() {
  const langToggleBtn = document.getElementById('langToggleBtn');
  const langLabel = document.getElementById('langLabel');
  if (!langToggleBtn) return;

  langToggleBtn.addEventListener('click', () => {
    currentLang = currentLang === 'ne' ? 'en' : 'ne';
    if (langLabel) {
      langLabel.textContent = currentLang === 'ne' ? 'English' : 'नेपाली';
    }

    // Update all elements with data-ne and data-en
    document.querySelectorAll('[data-ne][data-en]').forEach(el => {
      const text = currentLang === 'ne' ? el.getAttribute('data-ne') : el.getAttribute('data-en');
      if (text) {
        el.textContent = text;
      }
    });
  });
}

/* =========================================================
   6. SOCIAL SHARING & ACTION UTILITIES
   ========================================================= */
function initSocialSharing() {
  const shareWhatsappBtn = document.getElementById('shareWhatsappBtn');
  const copyMessageBtn = document.getElementById('copyMessageBtn');
  const toast = document.getElementById('copyToast');

  const inviteMessage = `💍 *शुभ विवाह निमन्त्रणा* 💍
विकल दाहाल र श्रद्धा दुलाल

श्री गणेशाय नम:
मंगलम् भगवान् विष्णुः मङ्गलम् गरुडध्वजः ।
मङ्गलम् पुण्डरीकाक्षः मङ्गलाय तनो हरी ॥

यही मिति २०८३ साल मंसिर १० गते बिहीबार हुने विकल र श्रद्धाको शुभ-विवाहको पावन अवसरमा यहाँहरूको गरिमामय उपस्थितिको लागि सादर निमन्त्रणा गर्दछौं।

🚩 *जन्ति प्रस्थान एवं शुभ-विवाह:*
मिति: २०८३ मंसिर १० गते (बिहीबार) | बिहान ८:०० बजे
स्थान: निजी निवास (पथरी) बाट बराहक्षेत्र-२, सुनसरी

🍽️ *प्रीतिभोज (Wedding Reception):*
मिति: २०८३ मंसिर ११ गते (शुक्रबार) | दिनको १:०० बजेदेखि
स्थान: निजी निवास, पथरी शनिश्चरे-२, मोरङ

📞 सम्पर्क: ९८४२०९६८४१, ९८६२३२५५२३, ९८४००३६९२५
दाहाल परिवार`;

  if (shareWhatsappBtn) {
    shareWhatsappBtn.addEventListener('click', () => {
      const currentUrl = window.location.href;
      const fullText = encodeURIComponent(`${inviteMessage}\n\nडिजिटल कार्ड हेर्नुहोस्:\n${currentUrl}`);
      window.open(`https://api.whatsapp.com/send?text=${fullText}`, '_blank');
    });
  }

  if (copyMessageBtn) {
    copyMessageBtn.addEventListener('click', () => {
      const currentUrl = window.location.href;
      const fullText = `${inviteMessage}\n\nडिजिटल कार्ड हेर्नुहोस्:\n${currentUrl}`;

      navigator.clipboard.writeText(fullText).then(() => {
        showToast('निमन्त्रणा सन्देश कपी गरियो! (Invitation text copied!)');
      }).catch(() => {
        showToast('कपी गर्न सकिएन, कृपया म्यानुअल्ली कपी गर्नुहोस्।');
      });
    });
  }

  function showToast(msg) {
    if (!toast) return;
    toast.textContent = msg;
    toast.style.display = 'block';
    setTimeout(() => {
      toast.style.display = 'none';
    }, 3200);
  }
}

// Google Calendar Helper
window.addToGoogleCalendar = function(eventType) {
  let title, details, location, start, end;

  if (eventType === 'janti') {
    title = encodeURIComponent('विकल र श्रद्धाको विवाह (Janti & Wedding) - Bikal & Shraddha');
    details = encodeURIComponent('विकल दाहाल र श्रद्धा दुलालको शुभ-विवाह एवं जन्ति प्रस्थान। सम्पर्क: 9842096841');
    location = encodeURIComponent('Barahakshetra-2, Udayachowk, Sunsari, Nepal');
    start = '20261126T021500Z'; // 08:00 AM NPT in UTC (08:00 - 05:45 = 02:15)
    end = '20261126T120000Z';
  } else {
    title = encodeURIComponent('विकल र श्रद्धाको प्रीतिभोज (Wedding Reception) - Bikal & Shraddha');
    details = encodeURIComponent('विकल र श्रद्धाको वैवाहिक प्रीतिभोज (Wedding Reception)। सम्पर्क: 9842096841');
    location = encodeURIComponent('Pathari Sanischare-2, Morang, Nepal');
    start = '20261127T071500Z'; // 01:00 PM NPT in UTC (13:00 - 05:45 = 07:15)
    end = '20261127T140000Z';
  }

  const gcalUrl = `https://calendar.google.com/calendar/render?action=TEMPLATE&text=${title}&dates=${start}/${end}&details=${details}&location=${location}`;
  window.open(gcalUrl, '_blank');
};

/* =========================================================
   7. BRIDE PHOTO GALLERY LIGHTBOX
   ========================================================= */
function initGalleryModal() {
  const modal = document.getElementById('galleryModal');
  const triggerBtn = document.getElementById('viewGalleryBtn');
  const closeBtn = document.getElementById('closeGalleryBtn');
  const activeImg = document.getElementById('galleryActiveImg');
  const prevBtn = document.getElementById('galleryPrevBtn');
  const nextBtn = document.getElementById('galleryNextBtn');
  const counterEl = document.getElementById('galleryCounter');
  const thumbsRow = document.getElementById('thumbnailsRow');

  if (!modal || !triggerBtn) return;

  const photos = [
    'bride.jpg',
    'bride_gallery_1.jpg',
    'bride_gallery_2.jpg',
    'bride_gallery_3.jpg',
    'bride_gallery_4.jpg'
  ];

  let currentIndex = 0;

  // Render thumbnails
  if (thumbsRow) {
    thumbsRow.innerHTML = '';
    photos.forEach((src, idx) => {
      const img = document.createElement('img');
      img.src = src;
      img.className = 'thumb-img' + (idx === 0 ? ' active' : '');
      img.addEventListener('click', () => setSlide(idx));
      thumbsRow.appendChild(img);
    });
  }

  function setSlide(index) {
    currentIndex = (index + photos.length) % photos.length;
    if (activeImg) activeImg.src = photos[currentIndex];
    if (counterEl) counterEl.textContent = `${currentIndex + 1} / ${photos.length}`;

    // Update active thumb
    const thumbs = thumbsRow.querySelectorAll('.thumb-img');
    thumbs.forEach((t, i) => {
      t.classList.toggle('active', i === currentIndex);
    });
  }

  triggerBtn.addEventListener('click', () => {
    modal.classList.add('active');
    setSlide(0);
  });

  if (closeBtn) closeBtn.addEventListener('click', () => modal.classList.remove('active'));
  if (prevBtn) prevBtn.addEventListener('click', () => setSlide(currentIndex - 1));
  if (nextBtn) nextBtn.addEventListener('click', () => setSlide(currentIndex + 1));

  modal.addEventListener('click', (e) => {
    if (e.target === modal) modal.classList.remove('active');
  });

  // Keyboard navigation
  window.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('active')) return;
    if (e.key === 'ArrowLeft') setSlide(currentIndex - 1);
    if (e.key === 'ArrowRight') setSlide(currentIndex + 1);
    if (e.key === 'Escape') modal.classList.remove('active');
  });
}

/* =========================================================
   8. ORIGINAL PRINTED CARD MODAL
   ========================================================= */
function initOriginalCardModal() {
  const modal = document.getElementById('originalCardModal');
  const triggerBtn = document.getElementById('viewOriginalCardBtn');
  const closeBtn = document.getElementById('closeOriginalCardBtn');

  if (!modal || !triggerBtn) return;

  triggerBtn.addEventListener('click', () => modal.classList.add('active'));
  if (closeBtn) closeBtn.addEventListener('click', () => modal.classList.remove('active'));

  modal.addEventListener('click', (e) => {
    if (e.target === modal) modal.classList.remove('active');
  });

  window.addEventListener('keydown', (e) => {
    if (modal.classList.contains('active') && e.key === 'Escape') {
      modal.classList.remove('active');
    }
  });
}
