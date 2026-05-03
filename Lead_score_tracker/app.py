import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Coolmate — Tech-Wear Demo",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
</style>
""", unsafe_allow_html=True)

HTML = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Coolmate</title>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box;}
:root{
  --navy:#3b4e6e;--navy-d:#2a3a54;
  --teal:#5bbfb5;--teal-l:#e0f5f3;--teal-d:#429b93;
  --orange:#f4a27c;--orange-d:#e8875a;
  --gray:#f4f6f8;--gray-2:#eef1f5;
  --dark:#334155;--mid:#7a8ea8;--border:#dde4ed;
  --sky:#7ab8e8;--purple:#9b85d4;
}
body{font-family:'Be Vietnam Pro',sans-serif;background:#f7f9fc;color:var(--dark);}

.topbar{background:linear-gradient(90deg,var(--navy-d),var(--navy));color:rgba(255,255,255,.7);font-size:12px;text-align:center;padding:7px 0;letter-spacing:.04em;}
.topbar span{color:#a8e6e1;}

nav{display:flex;align-items:center;justify-content:space-between;padding:0 40px;height:60px;border-bottom:1px solid var(--border);position:sticky;top:0;background:rgba(255,255,255,.95);backdrop-filter:blur(8px);z-index:100;box-shadow:0 1px 12px rgba(59,78,110,.07);}
.logo{font-size:22px;font-weight:800;color:var(--navy);letter-spacing:-.5px;cursor:pointer;}
.logo span{color:var(--teal);}
.nav-links{display:flex;gap:28px;}
.nav-links a{font-size:13.5px;font-weight:500;color:var(--dark);text-decoration:none;cursor:pointer;padding:4px 0;border-bottom:2px solid transparent;transition:all .2s;}
.nav-links a:hover,.nav-links a.active{color:var(--teal);border-bottom-color:var(--teal);}
.nav-right{display:flex;align-items:center;gap:20px;}
.nav-icon{width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:16px;transition:all .15s;}
.nav-icon:hover{background:var(--gray);}
.cart-badge{position:relative;}
.badge{position:absolute;top:-4px;right:-4px;background:var(--orange);color:#fff;font-size:10px;font-weight:700;width:16px;height:16px;border-radius:50%;display:flex;align-items:center;justify-content:center;}

.hero{background:linear-gradient(135deg,var(--navy-d) 55%,#4a6280);color:#fff;padding:60px 40px;display:flex;align-items:center;gap:60px;}
.hero-text{flex:1;}
.hero-badge{display:inline-block;background:rgba(91,191,181,.2);border:1px solid rgba(91,191,181,.4);color:#a8e6e1;font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:5px 12px;border-radius:20px;margin-bottom:16px;}
.hero h1{font-size:40px;font-weight:800;line-height:1.15;margin-bottom:14px;}
.hero h1 em{color:#a8e6e1;font-style:normal;}
.hero p{font-size:15px;color:rgba(255,255,255,.6);line-height:1.7;max-width:440px;margin-bottom:28px;}
.hero-btns{display:flex;gap:12px;}
.btn{padding:12px 24px;border-radius:10px;font-size:14px;font-weight:600;cursor:pointer;border:none;transition:all .15s;font-family:inherit;}
.btn-primary{background:var(--teal);color:#fff;}
.btn-primary:hover{background:var(--teal-d);transform:translateY(-1px);}
.btn-outline{background:transparent;color:#fff;border:1.5px solid rgba(255,255,255,.3);}
.btn-outline:hover{background:rgba(255,255,255,.08);}
.hero-img{width:320px;height:360px;background:rgba(255,255,255,.06);border-radius:20px;display:flex;flex-direction:column;align-items:center;justify-content:center;cursor:pointer;transition:all .2s;border:1px solid rgba(255,255,255,.12);}
.hero-img:hover{background:rgba(255,255,255,.1);transform:translateY(-4px);}
.hero-img-icon{font-size:80px;margin-bottom:12px;}
.hero-img-label{font-size:13px;color:rgba(255,255,255,.35);}

.trust{display:flex;border-bottom:1px solid var(--border);background:#fff;}
.trust-item{flex:1;padding:18px 24px;display:flex;align-items:center;gap:12px;border-right:1px solid var(--border);cursor:pointer;transition:all .15s;}
.trust-item:last-child{border-right:none;}
.trust-item:hover{background:var(--teal-l);}
.trust-icon{font-size:22px;}
.trust-text strong{display:block;font-weight:700;color:var(--navy);font-size:13.5px;}
.trust-text span{color:var(--mid);font-size:13px;}

.section{padding:56px 40px;background:#fff;}
.section-head{display:flex;align-items:baseline;gap:16px;margin-bottom:32px;}
.section-head h2{font-size:24px;font-weight:800;color:var(--navy);}
.section-head a{font-size:13px;color:var(--teal);cursor:pointer;font-weight:600;}
.products{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;}
.product-card{border:1.5px solid var(--border);border-radius:16px;overflow:hidden;cursor:pointer;transition:all .22s;background:#fff;}
.product-card:hover{box-shadow:0 10px 36px rgba(59,78,110,.12);transform:translateY(-4px);border-color:var(--teal);}
.product-thumb{height:200px;display:flex;align-items:center;justify-content:center;font-size:56px;position:relative;}
.product-tag{position:absolute;top:10px;left:10px;color:#fff;font-size:10px;font-weight:700;padding:3px 8px;border-radius:20px;background:var(--orange);}
.product-tag.new{background:var(--teal);}
.product-info{padding:14px 16px;}
.product-name{font-size:14px;font-weight:700;margin-bottom:4px;color:var(--navy);}
.product-sub{font-size:12px;color:var(--mid);margin-bottom:10px;}
.price-now{font-size:16px;font-weight:700;color:var(--teal);}
.price-old{font-size:13px;color:var(--mid);text-decoration:line-through;margin-left:6px;}
.product-actions{display:flex;gap:8px;margin-top:12px;}
.btn-add{flex:1;background:var(--navy);color:#fff;border:none;padding:9px;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer;font-family:inherit;transition:all .15s;}
.btn-add:hover{background:var(--teal);}
.btn-wish{width:36px;height:36px;border:1.5px solid var(--border);border-radius:8px;background:#fff;cursor:pointer;font-size:16px;display:flex;align-items:center;justify-content:center;transition:all .15s;}
.btn-wish:hover{background:var(--teal-l);border-color:var(--teal);}

.product-detail{padding:56px 40px;background:var(--gray);display:grid;grid-template-columns:1fr 1fr;gap:48px;}
.pd-img{background:#fff;border-radius:20px;height:440px;display:flex;align-items:center;justify-content:center;font-size:100px;cursor:pointer;transition:all .2s;border:1.5px solid var(--border);}
.pd-img:hover{background:var(--teal-l);border-color:var(--teal);}
.pd-badge{display:inline-block;background:var(--teal-l);color:var(--teal-d);font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;padding:4px 12px;border-radius:20px;margin-bottom:12px;}
.pd-name{font-size:26px;font-weight:800;color:var(--navy);margin-bottom:8px;line-height:1.25;}
.pd-rating{display:flex;align-items:center;gap:8px;margin-bottom:16px;cursor:pointer;}
.stars{color:#f4b860;font-size:14px;letter-spacing:1px;}
.rating-count{font-size:13px;color:var(--mid);}
.pd-price{display:flex;align-items:baseline;gap:12px;margin-bottom:20px;}
.pd-price-now{font-size:28px;font-weight:800;color:var(--teal);}
.pd-price-old{font-size:16px;color:var(--mid);text-decoration:line-through;}
.pd-price-save{background:var(--orange);color:#fff;font-size:11px;font-weight:700;padding:3px 10px;border-radius:20px;}
.pd-tech{display:flex;gap:8px;margin-bottom:24px;flex-wrap:wrap;}
.tech-badge{background:#fff;border:1.5px solid var(--border);border-radius:20px;padding:6px 14px;font-size:12px;font-weight:600;color:var(--navy);cursor:pointer;transition:all .15s;}
.tech-badge:hover,.tech-badge.active{background:var(--teal-l);border-color:var(--teal);color:var(--teal-d);}
.pd-section-label{font-size:11px;font-weight:700;color:var(--mid);letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px;}
.size-row{display:flex;gap:8px;margin-bottom:20px;}
.size-btn{width:44px;height:44px;border:1.5px solid var(--border);border-radius:10px;background:#fff;font-size:13px;font-weight:600;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .15s;}
.size-btn:hover,.size-btn.active{background:var(--navy);color:#fff;border-color:var(--navy);}
.color-row{display:flex;gap:10px;margin-bottom:24px;}
.color-dot{width:28px;height:28px;border-radius:50%;cursor:pointer;border:2px solid transparent;transition:all .15s;}
.color-dot:hover,.color-dot.active{border-color:var(--navy);transform:scale(1.15);box-shadow:0 2px 8px rgba(0,0,0,.15);}
.pd-btns{display:flex;gap:12px;margin-bottom:20px;}
.btn-buy{flex:1;background:var(--orange);color:#fff;border:none;padding:14px;border-radius:12px;font-size:15px;font-weight:700;cursor:pointer;font-family:inherit;transition:all .15s;}
.btn-buy:hover{background:var(--orange-d);transform:translateY(-2px);}
.btn-cart{flex:1;background:var(--navy);color:#fff;border:none;padding:14px;border-radius:12px;font-size:15px;font-weight:700;cursor:pointer;font-family:inherit;transition:all .15s;}
.btn-cart:hover{background:var(--teal);}
.pd-guarantee{display:flex;gap:16px;padding:16px;background:#fff;border-radius:12px;border:1px solid var(--border);}
.guarantee-item{display:flex;align-items:center;gap:8px;font-size:12.5px;color:var(--mid);flex:1;}
.guarantee-item span:first-child{font-size:18px;}

.reviews{padding:48px 40px;background:#fff;}
.review-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:24px;}
.review-card{background:var(--gray-2);border-radius:14px;padding:20px;cursor:pointer;transition:all .15s;border:1.5px solid transparent;}
.review-card:hover{border-color:var(--teal);background:var(--teal-l);}
.review-header{display:flex;align-items:center;gap:10px;margin-bottom:10px;}
.review-avatar{width:36px;height:36px;border-radius:50%;background:var(--navy);color:#fff;font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center;}
.review-name{font-size:14px;font-weight:700;color:var(--navy);}
.review-date{font-size:11.5px;color:var(--mid);}
.review-body{font-size:13.5px;color:var(--dark);line-height:1.6;}

.signup-section{background:linear-gradient(135deg,var(--navy-d),#4a6280);padding:56px 40px;display:flex;align-items:center;justify-content:space-between;gap:40px;}
.signup-text h2{font-size:26px;font-weight:800;color:#fff;margin-bottom:8px;}
.signup-text p{font-size:14px;color:rgba(255,255,255,.55);line-height:1.6;}
.signup-form{display:flex;gap:10px;min-width:400px;}
.signup-input{flex:1;padding:13px 16px;border-radius:10px;border:1.5px solid rgba(255,255,255,.15);background:rgba(255,255,255,.1);color:#fff;font-size:14px;font-family:inherit;outline:none;transition:border-color .2s;}
.signup-input::placeholder{color:rgba(255,255,255,.35);}
.signup-input:focus{border-color:var(--teal);}
.btn-signup{background:var(--teal);color:#fff;border:none;padding:13px 22px;border-radius:10px;font-size:14px;font-weight:700;cursor:pointer;font-family:inherit;white-space:nowrap;}
.btn-signup:hover{background:var(--teal-d);}

footer{background:var(--navy-d);color:rgba(255,255,255,.45);padding:32px 40px;display:flex;align-items:center;justify-content:space-between;}
footer .logo{color:#fff;font-size:18px;}
.footer-links{display:flex;gap:24px;}
.footer-links a{font-size:13px;color:rgba(255,255,255,.4);cursor:pointer;transition:color .15s;}
.footer-links a:hover{color:#fff;}
footer p{font-size:12px;}

/* ══ LEAD WIDGET (fixed trong iframe — widget nhỏ, OK) ══ */
#lead-widget{position:fixed;right:20px;top:88px;background:#fff;border-radius:16px;width:212px;box-shadow:0 8px 32px rgba(59,78,110,.18);z-index:998;overflow:hidden;border:1.5px solid var(--border);}
.widget-header{background:linear-gradient(90deg,var(--teal-d),var(--sky));padding:10px 14px;font-size:10px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#fff;}
.widget-body{padding:14px;}
.score-ring-wrap{display:flex;justify-content:center;margin-bottom:6px;}
svg.ring{transform:rotate(-90deg);}
.ring-bg{fill:none;stroke:var(--gray);stroke-width:8;}
.ring-fg{fill:none;stroke-width:8;stroke-linecap:round;transition:stroke-dashoffset .5s cubic-bezier(.4,0,.2,1);}
.score-row{display:flex;align-items:baseline;gap:6px;justify-content:center;}
.score-num{font-size:34px;font-weight:800;color:var(--navy);line-height:1;transition:all .2s;}
.score-label{font-size:11px;color:var(--mid);}
.score-bar-bg{height:7px;background:var(--gray);border-radius:4px;margin:10px 0 6px;overflow:hidden;}
.score-bar{height:100%;border-radius:4px;background:linear-gradient(90deg,var(--teal),var(--sky));transition:width .45s cubic-bezier(.4,0,.2,1);}
.score-status{font-size:11px;font-weight:700;padding:3px 8px;border-radius:20px;display:inline-block;margin-bottom:10px;}
.score-status.cold{background:#e8f3fe;color:#4a88c7;}
.score-status.warm{background:#fff4e0;color:#c97a28;}
.score-status.mql{background:#e0f8f0;color:#2a9e72;}
.score-status.sql{background:#ffeee6;color:var(--orange-d);}
.events-log{border-top:1px solid var(--border);padding-top:10px;}
.log-title{font-size:9.5px;color:var(--mid);letter-spacing:.1em;text-transform:uppercase;margin-bottom:6px;}
.log-item{display:flex;justify-content:space-between;align-items:center;font-size:11px;margin-bottom:4px;animation:logIn .3s ease;}
@keyframes logIn{from{opacity:0;transform:translateY(-4px);}to{opacity:1;transform:translateY(0);}}
.log-action{color:var(--mid);flex:1;overflow:hidden;white-space:nowrap;text-overflow:ellipsis;}
.log-pts{background:var(--teal-l);color:var(--teal-d);font-weight:700;font-size:10px;padding:1px 6px;border-radius:10px;margin-left:4px;flex-shrink:0;}

/* FLASH */
.flash{position:fixed;top:72px;left:50%;transform:translateX(-50%);background:#fff;color:var(--dark);border-radius:12px;padding:9px 20px;font-size:13px;font-weight:600;z-index:9999;animation:flashA .95s ease both;pointer-events:none;white-space:nowrap;border:1.5px solid var(--border);display:flex;align-items:center;gap:10px;box-shadow:0 4px 20px rgba(59,78,110,.14);}
.flash-pts{color:var(--teal-d);font-size:15px;font-weight:700;}
@keyframes flashA{0%{opacity:0;transform:translateX(-50%) translateY(-10px);}18%{opacity:1;transform:translateX(-50%) translateY(0);}75%{opacity:1;}100%{opacity:0;transform:translateX(-50%) translateY(-6px);}}
.m-flash{position:fixed;top:72px;left:50%;transform:translateX(-50%);color:#fff;border-radius:12px;padding:10px 22px;font-size:14px;font-weight:700;z-index:9999;pointer-events:none;white-space:nowrap;animation:flashA 2.2s ease both;}
.pulse{animation:pulseA .28s ease both;}
@keyframes pulseA{0%{transform:scale(1);}50%{transform:scale(1.2);}100%{transform:scale(1);}}
</style>
</head>
<body>

<!-- LEAD WIDGET -->
<div id="lead-widget">
  <div class="widget-header">🎯 HubSpot Lead Tracker</div>
  <div class="widget-body">
    <div class="score-ring-wrap">
      <svg class="ring" width="74" height="74" viewBox="0 0 74 74">
        <circle class="ring-bg" cx="37" cy="37" r="29"/>
        <circle class="ring-fg" id="ring-fg" cx="37" cy="37" r="29"
          stroke="url(#rg)" stroke-dasharray="182.21" stroke-dashoffset="182.21"/>
        <defs>
          <linearGradient id="rg" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="#5bbfb5"/>
            <stop offset="100%" stop-color="#7ab8e8"/>
          </linearGradient>
        </defs>
      </svg>
    </div>
    <div class="score-row">
      <div class="score-num" id="score-num">0</div>
      <div class="score-label">/ 100</div>
    </div>
    <div class="score-bar-bg"><div class="score-bar" id="score-bar" style="width:0%"></div></div>
    <div style="margin-top:4px;margin-bottom:10px;">
      <span class="score-status cold" id="score-status">❄️ Cold Lead</span>
    </div>
    <div class="events-log">
      <div class="log-title">Hành động gần nhất</div>
      <div id="log-list">
        <div class="log-item"><span class="log-action" style="font-style:italic;">Chưa có tương tác...</span></div>
      </div>
    </div>
  </div>
</div>

<!-- TOPBAR -->
<div class="topbar">Miễn phí vận chuyển đơn từ <span>399.000đ</span> · Đổi trả 30 ngày · 1800-xxxx</div>

<!-- NAV -->
<nav>
  <div class="logo" data-action="Xem logo" data-pts="1">Cool<span>mate</span></div>
  <div class="nav-links">
    <a class="active" data-action="Trang chủ" data-pts="2">Trang chủ</a>
    <a data-action="Xem danh mục Nam" data-pts="3">Nam</a>
    <a data-action="Xem Tech-Wear" data-pts="5">Tech-Wear</a>
    <a data-action="Xem Ex-Dry" data-pts="4">Ex-Dry</a>
    <a data-action="Xem Anti-Smell" data-pts="4">Anti-Smell</a>
    <a data-action="Xem CoolClub" data-pts="6">CoolClub</a>
  </div>
  <div class="nav-right">
    <div class="nav-icon" data-action="Tìm kiếm" data-pts="4">🔍</div>
    <div class="nav-icon" data-action="Yêu thích" data-pts="3">🤍</div>
    <div class="nav-icon cart-badge" data-action="Mở giỏ hàng" data-pts="8">🛒<span class="badge">0</span></div>
    <div class="nav-icon" data-action="Đăng nhập" data-pts="7">👤</div>
  </div>
</nav>

<!-- HERO -->
<div class="hero">
  <div class="hero-text">
    <div class="hero-badge">✨ Bộ sưu tập mới 2025</div>
    <h1>Tech-Wear<br>Từ <em>Văn Phòng</em><br>Đến Phòng Tập</h1>
    <p>Vải Ex-Dry thấm hút nhanh, công nghệ Anti-Smell kháng khuẩn 24h — thoải mái từ buổi họp đến buổi gym.</p>
    <div class="hero-btns">
      <button class="btn btn-primary" data-action="Khám phá bộ sưu tập" data-pts="8">Khám phá ngay</button>
      <button class="btn btn-outline" data-action="Xem video giới thiệu" data-pts="5">Xem video ▶</button>
    </div>
  </div>
  <div class="hero-img" data-action="Xem ảnh hero" data-pts="4">
    <div class="hero-img-icon">👕</div>
    <div class="hero-img-label">Click để khám phá</div>
  </div>
</div>

<!-- TRUST -->
<div class="trust">
  <div class="trust-item" data-action="Xem thông tin Ex-Dry" data-pts="4"><span class="trust-icon">💧</span><div class="trust-text"><strong>Công nghệ Ex-Dry</strong><span>Thấm hút cực nhanh</span></div></div>
  <div class="trust-item" data-action="Xem Anti-Smell" data-pts="4"><span class="trust-icon">🛡️</span><div class="trust-text"><strong>Anti-Smell 24h</strong><span>Kháng khuẩn, khử mùi</span></div></div>
  <div class="trust-item" data-action="Xem chính sách đổi trả" data-pts="6"><span class="trust-icon">🔄</span><div class="trust-text"><strong>Đổi trả 30 ngày</strong><span>Không cần lý do</span></div></div>
  <div class="trust-item" data-action="Xem cam kết chính hãng" data-pts="3"><span class="trust-icon">✅</span><div class="trust-text"><strong>Hàng chính hãng</strong><span>Made in Vietnam</span></div></div>
</div>

<!-- PRODUCTS -->
<div class="section">
  <div class="section-head"><h2>Bán chạy nhất</h2><a data-action="Xem tất cả sản phẩm" data-pts="5">Xem tất cả →</a></div>
  <div class="products">
    <div class="product-card" data-action="Xem áo Polo Ex-Dry" data-pts="5">
      <div class="product-thumb" style="background:#e6f6f4;"><div class="product-tag new">Mới</div>👕</div>
      <div class="product-info">
        <div class="product-name">Áo Polo Ex-Dry Tech</div><div class="product-sub">Thấm hút nhanh</div>
        <div><span class="price-now">449.000đ</span><span class="price-old">599.000đ</span></div>
        <div class="product-actions">
          <button class="btn-add" data-action="Thêm giỏ — Polo Ex-Dry" data-pts="15">Thêm giỏ hàng</button>
          <button class="btn-wish" data-action="Yêu thích — Polo" data-pts="4">🤍</button>
        </div>
      </div>
    </div>
    <div class="product-card" data-action="Xem Quần Jogger Anti-Smell" data-pts="5">
      <div class="product-thumb" style="background:#fdf0eb;"><div class="product-tag">-25%</div>🩲</div>
      <div class="product-info">
        <div class="product-name">Quần Jogger Anti-Smell</div><div class="product-sub">Kháng khuẩn, co giãn 4D</div>
        <div><span class="price-now">559.000đ</span><span class="price-old">749.000đ</span></div>
        <div class="product-actions">
          <button class="btn-add" data-action="Thêm giỏ — Jogger" data-pts="15">Thêm giỏ hàng</button>
          <button class="btn-wish" data-action="Yêu thích — Jogger" data-pts="4">🤍</button>
        </div>
      </div>
    </div>
    <div class="product-card" data-action="Xem Áo Thun Kỹ Thuật" data-pts="5">
      <div class="product-thumb" style="background:#edf0ff;"><div class="product-tag new">Mới</div>👔</div>
      <div class="product-info">
        <div class="product-name">Áo Thun Kỹ Thuật Pro</div><div class="product-sub">Ex-Dry + Anti-Smell</div>
        <div><span class="price-now">349.000đ</span><span class="price-old">429.000đ</span></div>
        <div class="product-actions">
          <button class="btn-add" data-action="Thêm giỏ — Áo Thun" data-pts="15">Thêm giỏ hàng</button>
          <button class="btn-wish" data-action="Yêu thích — Áo Thun" data-pts="4">🤍</button>
        </div>
      </div>
    </div>
    <div class="product-card" data-action="Xem Combo Tech-Wear" data-pts="7">
      <div class="product-thumb" style="background:#f3effb;"><div class="product-tag" style="background:#9b85d4;">Combo</div>🎁</div>
      <div class="product-info">
        <div class="product-name">Combo Tech-Wear Office</div><div class="product-sub">1 Polo + 1 Thun + 1 Jogger</div>
        <div><span class="price-now">999.000đ</span><span class="price-old">1.399.000đ</span></div>
        <div class="product-actions">
          <button class="btn-add" data-action="Thêm giỏ — Combo" data-pts="20">Thêm giỏ hàng</button>
          <button class="btn-wish" data-action="Yêu thích — Combo" data-pts="4">🤍</button>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- PRODUCT DETAIL -->
<div class="product-detail">
  <div class="pd-img" data-action="Xem ảnh chi tiết" data-pts="6">👕</div>
  <div>
    <div class="pd-badge">Bestseller · 4.8★ · 1.240 đánh giá</div>
    <div class="pd-name">Áo Polo Ex-Dry Kỹ Thuật Pro 2025</div>
    <div class="pd-rating" data-action="Xem đánh giá" data-pts="4"><span class="stars">★★★★★</span><span class="rating-count">4.8 (1.240 đánh giá)</span></div>
    <div class="pd-price"><span class="pd-price-now">449.000đ</span><span class="pd-price-old">599.000đ</span><span class="pd-price-save">Giảm 25%</span></div>
    <div class="pd-section-label">Công nghệ</div>
    <div class="pd-tech">
      <div class="tech-badge active" data-action="Xem Ex-Dry" data-pts="5">⚡ Ex-Dry</div>
      <div class="tech-badge" data-action="Xem Anti-Smell" data-pts="5">🛡️ Anti-Smell</div>
      <div class="tech-badge" data-action="Xem co giãn 4D" data-pts="5">🔄 Co giãn 4D</div>
      <div class="tech-badge" data-action="Xem bảng size" data-pts="6">📐 Bảng size</div>
    </div>
    <div class="pd-section-label">Kích thước</div>
    <div class="size-row">
      <div class="size-btn" data-action="Chọn size S" data-pts="3">S</div>
      <div class="size-btn active" data-action="Chọn size M" data-pts="3">M</div>
      <div class="size-btn" data-action="Chọn size L" data-pts="3">L</div>
      <div class="size-btn" data-action="Chọn size XL" data-pts="3">XL</div>
      <div class="size-btn" data-action="Chọn size XXL" data-pts="3">XXL</div>
    </div>
    <div class="pd-section-label">Màu sắc</div>
    <div class="color-row">
      <div class="color-dot active" style="background:#334155;" data-action="Chọn màu đen" data-pts="3"></div>
      <div class="color-dot" style="background:#5bbfb5;" data-action="Chọn màu xanh ngọc" data-pts="3"></div>
      <div class="color-dot" style="background:#7ab8e8;" data-action="Chọn màu xanh dương" data-pts="3"></div>
      <div class="color-dot" style="background:#f4829a;" data-action="Chọn màu hồng" data-pts="3"></div>
      <div class="color-dot" style="background:#d1d9e6;" data-action="Chọn màu xám" data-pts="3"></div>
    </div>
    <div class="pd-btns">
      <button class="btn-buy" data-action="Mua ngay — Polo" data-pts="25">⚡ Mua ngay</button>
      <button class="btn-cart" data-action="Thêm giỏ — Polo chi tiết" data-pts="15">🛒 Thêm giỏ</button>
    </div>
    <div class="pd-guarantee">
      <div class="guarantee-item"><span>🔄</span><span>Đổi trả 30 ngày</span></div>
      <div class="guarantee-item"><span>🚚</span><span>Giao nhanh 2h</span></div>
      <div class="guarantee-item"><span>✅</span><span>Chính hãng 100%</span></div>
    </div>
  </div>
</div>

<!-- REVIEWS -->
<div class="reviews">
  <div class="section-head"><h2>Đánh giá từ khách hàng</h2><a data-action="Xem tất cả đánh giá" data-pts="5">Xem thêm →</a></div>
  <div class="review-grid">
    <div class="review-card" data-action="Đọc review Minh Hoàng" data-pts="4">
      <div class="review-header"><div class="review-avatar">MH</div><div><div class="review-name">Minh Hoàng</div><div class="review-date">★★★★★ · 2 ngày trước</div></div></div>
      <div class="review-body">Mặc đi làm cả ngày rồi đi gym vẫn không bị mùi. Vải thoáng mát, form đẹp!</div>
    </div>
    <div class="review-card" data-action="Đọc review Thu Hằng" data-pts="4">
      <div class="review-header"><div class="review-avatar" style="background:var(--teal);">TH</div><div><div class="review-name">Thu Hằng</div><div class="review-date">★★★★★ · 5 ngày trước</div></div></div>
      <div class="review-body">Mua tặng chồng, anh ấy thích lắm. Vải mềm, ship nhanh. 5 sao!</div>
    </div>
    <div class="review-card" data-action="Đọc review Đức Anh" data-pts="4">
      <div class="review-header"><div class="review-avatar" style="background:var(--orange);">ĐA</div><div><div class="review-name">Đức Anh</div><div class="review-date">★★★★☆ · 1 tuần trước</div></div></div>
      <div class="review-body">Đã mua lần 3 vẫn chưa thất vọng. Bền và thoải mái.</div>
    </div>
  </div>
</div>

<!-- SIGNUP -->
<div class="signup-section">
  <div class="signup-text">
    <h2>Nhận ưu đãi độc quyền CoolClub</h2>
    <p>Đăng ký nhận voucher thành viên và tips mặc đẹp mỗi tuần.</p>
  </div>
  <div class="signup-form">
    <input class="signup-input" type="email" placeholder="Nhập email của bạn..."
           data-action="Điền email CoolClub" data-pts="12" id="email-input">
    <button class="btn-signup" data-action="Đăng ký CoolClub" data-pts="18">Đăng ký ngay</button>
  </div>
</div>

<!-- FOOTER -->
<footer>
  <div class="logo" data-action="Click logo footer" data-pts="1">Cool<span style="color:var(--teal)">mate</span></div>
  <div class="footer-links">
    <a data-action="Bảo mật" data-pts="4">Bảo mật</a>
    <a data-action="Điều khoản" data-pts="3">Điều khoản</a>
    <a data-action="Liên hệ" data-pts="6">Liên hệ</a>
    <a data-action="FAQ" data-pts="5">FAQ</a>
  </div>
  <p>© 2025 Coolmate. Made in Vietnam 🇻🇳</p>
</footer>

<script>
// ══════════════════════════════════════════════════
//  ZALO POPUP — inject thẳng vào parent DOM
//  window.parent.document (same-origin srcdoc iframe)
// ══════════════════════════════════════════════════
const ZALO_MSGS = {
  20: `<span style="color:#0068ff;font-weight:700;">Minh Hoàng ơi!</span> 👋<br>
       Mình thấy bạn đang xem <b>Tech-Wear</b> — vải Ex-Dry mặc cả ngày không bị mùi luôn!<br><br>
       Dùng mã <span style="display:inline-block;background:#fff4e0;color:#c97a28;font-weight:700;padding:1px 8px;border-radius:6px;font-size:13px;border:1px dashed #f4b860;">FREESHIP</span> miễn phí vận chuyển đơn đầu. Hết hạn <b>hôm nay</b> thôi! ⏰`,
  40: `<span style="color:#0068ff;font-weight:700;">Minh Hoàng ơi!</span> 🎉<br>
       HubSpot ghi nhận bạn là <b>MQL</b> rồi — đang cân nhắc thật sự đó!<br><br>
       Tặng riêng mã <span style="display:inline-block;background:#fff4e0;color:#c97a28;font-weight:700;padding:1px 8px;border-radius:6px;font-size:13px;border:1px dashed #f4b860;">VIP15</span> giảm thêm <b>15%</b> Combo Tech-Wear. Chỉ còn <b>3 suất</b> hôm nay! 👑`,
  70: `<span style="color:#0068ff;font-weight:700;">Minh Hoàng ơi!</span> 🚀<br>
       Score đạt <b>SQL</b> rồi — CSKH đang online, tư vấn 1:1 ngay!<br><br>
       Đặt trong <b>30 phút</b> nhận mã <span style="display:inline-block;background:#fff4e0;color:#c97a28;font-weight:700;padding:1px 8px;border-radius:6px;font-size:13px;border:1px dashed #f4b860;">GYMSET</span> tặng kèm <b>túi gym miễn phí</b>. Chỉ 2 suất! 🎁`
};

const ZALO_CSS = `
  #cm-zalo-wrap {
    position: fixed;
    top: 24px;
    left: 24px;
    width: 330px;
    z-index: 2147483647;
    font-family: 'Be Vietnam Pro', -apple-system, sans-serif;
    transform: translateX(-120%);
    opacity: 0;
    transition: transform .5s cubic-bezier(.34,1.56,.64,1), opacity .32s ease;
    pointer-events: none;
  }
  #cm-zalo-wrap.cm-show {
    transform: translateX(0);
    opacity: 1;
    pointer-events: all;
  }
  #cm-zalo-wrap * { box-sizing: border-box; margin: 0; padding: 0; }
  .cm-card {
    background: #fff;
    border-radius: 18px;
    box-shadow: 0 20px 60px rgba(0,104,255,.2), 0 4px 18px rgba(0,0,0,.1);
    overflow: hidden;
    border: 1.5px solid #d4e8fb;
  }
  .cm-hdr {
    background: linear-gradient(90deg,#0068ff,#1a90ff);
    padding: 10px 14px;
    display: flex; align-items: center; gap: 10px;
  }
  .cm-logo {
    width:28px;height:28px;background:#fff;border-radius:8px;
    display:flex;align-items:center;justify-content:center;
    font-size:15px;font-weight:900;color:#0068ff;
    font-family:sans-serif;flex-shrink:0;
  }
  .cm-hdr-txt { flex:1; }
  .cm-app { font-size:11px;font-weight:700;color:#fff; }
  .cm-sub { font-size:10px;color:rgba(255,255,255,.65); }
  .cm-close {
    background:rgba(255,255,255,.2);border:none;color:#fff;
    width:22px;height:22px;border-radius:50%;cursor:pointer;
    font-size:13px;line-height:1;
    display:flex;align-items:center;justify-content:center;
    flex-shrink:0;
  }
  .cm-close:hover{background:rgba(255,255,255,.38);}
  .cm-body { padding:14px 16px 10px; }
  .cm-sender { display:flex;align-items:center;gap:10px;margin-bottom:10px; }
  .cm-avatar {
    width:38px;height:38px;border-radius:50%;
    background:linear-gradient(135deg,#5bbfb5,#7ab8e8);
    display:flex;align-items:center;justify-content:center;
    font-size:14px;font-weight:800;color:#fff;flex-shrink:0;
  }
  .cm-sname{font-size:13px;font-weight:700;color:#334155;}
  .cm-slbl{font-size:10.5px;color:#7a8ea8;}
  .cm-bubble {
    background:#f0f7ff;
    border-radius:4px 16px 16px 16px;
    padding:11px 14px;
    font-size:13.5px;color:#334155;line-height:1.6;
    border:1px solid #d4e8fb;position:relative;
  }
  .cm-bubble::before{
    content:'';position:absolute;top:0;left:-7px;
    border:7px solid transparent;
    border-right-color:#d4e8fb;border-top-color:#d4e8fb;
  }
  .cm-time{font-size:10px;color:#7a8ea8;text-align:right;padding:4px 16px 8px;}
  .cm-footer{display:flex;gap:8px;padding:0 14px 14px;}
  .cm-cta{
    flex:1;background:linear-gradient(90deg,#0068ff,#1a90ff);
    color:#fff;border:none;border-radius:10px;padding:9px;
    font-size:13px;font-weight:700;cursor:pointer;font-family:inherit;
  }
  .cm-later{
    background:#f4f6f8;color:#7a8ea8;border:none;border-radius:10px;
    padding:9px 14px;font-size:13px;font-weight:600;
    cursor:pointer;font-family:inherit;white-space:nowrap;
  }
  .cm-ping{
    display:inline-block;width:7px;height:7px;border-radius:50%;
    background:#22c55e;vertical-align:middle;margin-right:4px;
    animation:cmPing 1.5s infinite;
  }
  @keyframes cmPing{
    0%,100%{box-shadow:0 0 0 2px rgba(34,197,94,.3);}
    50%{box-shadow:0 0 0 5px rgba(34,197,94,.1);}
  }
  @keyframes cmSlide{
    0%{opacity:0;transform:translateX(-120%);}
    100%{opacity:1;transform:translateX(0);}
  }
`;

let zpTimer = null;

function injectZaloIfNeeded() {
  try {
    const parent = window.parent;
    const pdoc = parent.document;

    // Inject style once
    if (!pdoc.getElementById('cm-zalo-style')) {
      const st = pdoc.createElement('style');
      st.id = 'cm-zalo-style';
      st.textContent = ZALO_CSS;
      pdoc.head.appendChild(st);
    }

    // Inject Google Font once
    if (!pdoc.getElementById('cm-zalo-font')) {
      const lk = pdoc.createElement('link');
      lk.id = 'cm-zalo-font';
      lk.rel = 'stylesheet';
      lk.href = 'https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;600;700;800&display=swap';
      pdoc.head.appendChild(lk);
    }

    // Create wrapper if not present
    if (!pdoc.getElementById('cm-zalo-wrap')) {
      const now = new Date();
      const timeStr = now.getHours() + ':' + String(now.getMinutes()).padStart(2,'0') + ' · vừa xong';
      const wrap = pdoc.createElement('div');
      wrap.id = 'cm-zalo-wrap';
      wrap.innerHTML = `
        <div class="cm-card">
          <div class="cm-hdr">
            <div class="cm-logo">Z</div>
            <div class="cm-hdr-txt">
              <div class="cm-app">Zalo · Coolmate Official</div>
              <div class="cm-sub"><span class="cm-ping"></span>vừa nhắn tin cho bạn</div>
            </div>
            <button class="cm-close" id="cm-close-btn">✕</button>
          </div>
          <div class="cm-body">
            <div class="cm-sender">
              <div class="cm-avatar">CM</div>
              <div>
                <div class="cm-sname">Coolmate CSKH</div>
                <div class="cm-slbl">Nhân viên tư vấn · Online ngay</div>
              </div>
            </div>
            <div class="cm-bubble" id="cm-msg">...</div>
          </div>
          <div class="cm-time" id="cm-time">${timeStr}</div>
          <div class="cm-footer">
            <button class="cm-cta" id="cm-cta-btn">Đặt hàng ngay 🛒</button>
            <button class="cm-later" id="cm-later-btn">Để sau</button>
          </div>
        </div>`;
      pdoc.body.appendChild(wrap);

      // Bind dismiss handlers
      const dismiss = () => {
        clearTimeout(zpTimer);
        wrap.classList.remove('cm-show');
      };
      pdoc.getElementById('cm-close-btn').onclick = dismiss;
      pdoc.getElementById('cm-cta-btn').onclick = dismiss;
      pdoc.getElementById('cm-later-btn').onclick = dismiss;
    }

    return true;
  } catch(e) {
    // cross-origin blocked — fallback
    return false;
  }
}

function triggerZalo(milestone) {
  const ok = injectZaloIfNeeded();
  if (!ok) return;

  try {
    const pdoc = window.parent.document;
    const now = new Date();
    pdoc.getElementById('cm-msg').innerHTML = ZALO_MSGS[milestone] || '';
    pdoc.getElementById('cm-time').textContent =
      now.getHours() + ':' + String(now.getMinutes()).padStart(2,'0') + ' · vừa xong';

    clearTimeout(zpTimer);
    setTimeout(() => {
      pdoc.getElementById('cm-zalo-wrap').classList.add('cm-show');
      zpTimer = setTimeout(() => {
        pdoc.getElementById('cm-zalo-wrap').classList.remove('cm-show');
      }, 9000);
    }, 700);
  } catch(e) {}
}

// ══════════════════════════════════════════════════
//  LEAD SCORE LOGIC
// ══════════════════════════════════════════════════
let score = 0, MAX = 100;
const logItems = [];
const CIRCUMF = 182.21;

const MILESTONES = {
  20: { label:'🔥 Warm Lead! HubSpot bắt đầu theo dõi', color:'#f4a27c' },
  40: { label:'⭐ Đạt MQL! AI kích hoạt Workflow',       color:'#5bbfb5' },
  70: { label:'🚀 SQL! Chuẩn bị được tư vấn 1:1',        color:'#9b85d4' }
};

function getStatus(s) {
  if (s < 20) return { cls:'cold', txt:'❄️ Cold Lead' };
  if (s < 40) return { cls:'warm', txt:'🔥 Warm Lead' };
  if (s < 70) return { cls:'mql',  txt:'⭐ MQL · Đủ điều kiện' };
  return            { cls:'sql',  txt:'🚀 SQL · Sẵn sàng mua!' };
}

function addScore(pts, action) {
  const prev = score;
  score = Math.min(score + pts, MAX);
  const pct = score / MAX;

  document.getElementById('score-num').textContent = score;
  document.getElementById('score-num').classList.add('pulse');
  setTimeout(() => document.getElementById('score-num').classList.remove('pulse'), 300);
  document.getElementById('score-bar').style.width = (pct * 100) + '%';
  document.getElementById('ring-fg').style.strokeDashoffset = CIRCUMF * (1 - pct);

  const { cls, txt } = getStatus(score);
  const ss = document.getElementById('score-status');
  ss.className = 'score-status ' + cls;
  ss.textContent = txt;

  [20, 40, 70].forEach(m => {
    if (prev < m && score >= m) {
      showMFlash(MILESTONES[m].label, MILESTONES[m].color);
      triggerZalo(m);
    }
  });

  addLog(action, pts);
  showFlashPts(action, pts);
}

function addLog(action, pts) {
  logItems.unshift({ action, pts });
  if (logItems.length > 4) logItems.pop();
  document.getElementById('log-list').innerHTML = logItems.map(i =>
    `<div class="log-item"><span class="log-action">${i.action}</span><span class="log-pts">+${i.pts}</span></div>`
  ).join('');
}

function showFlashPts(action, pts) {
  const el = document.createElement('div');
  el.className = 'flash';
  el.innerHTML = `<span>${action}</span><span class="flash-pts">+${pts}</span>`;
  document.body.appendChild(el);
  setTimeout(() => el.remove(), 980);
}

function showMFlash(label, color) {
  setTimeout(() => {
    const el = document.createElement('div');
    el.className = 'm-flash';
    el.style.background = color;
    el.style.boxShadow = `0 6px 24px ${color}55`;
    el.textContent = label;
    document.body.appendChild(el);
    setTimeout(() => el.remove(), 2300);
  }, 220);
}

document.addEventListener('click', e => {
  const el = e.target.closest('[data-pts]');
  if (!el) return;
  addScore(parseInt(el.dataset.pts), el.dataset.action || el.textContent.trim().slice(0,30));
  if (el.classList.contains('size-btn')) {
    el.closest('.size-row').querySelectorAll('.size-btn').forEach(b => b.classList.remove('active'));
    el.classList.add('active');
  }
  if (el.classList.contains('color-dot')) {
    el.closest('.color-row').querySelectorAll('.color-dot').forEach(b => b.classList.remove('active'));
    el.classList.add('active');
  }
  if (el.classList.contains('tech-badge')) {
    el.closest('.pd-tech').querySelectorAll('.tech-badge').forEach(b => b.classList.remove('active'));
    el.classList.add('active');
  }
  if (el.closest('.nav-links')) {
    const a = el.closest('a');
    if (a) {
      document.querySelectorAll('.nav-links a').forEach(l => l.classList.remove('active'));
      a.classList.add('active');
    }
  }
});

document.getElementById('email-input').addEventListener('focus', function() {
  addScore(parseInt(this.dataset.pts), this.dataset.action);
});
</script>
</body>
</html>"""

components.html(HTML, height=860, scrolling=True)
