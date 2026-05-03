# Coolmate x HubSpot: MarTech Strategy & CRM Architecture Simulation

Dự án này là một bản lộ trình toàn diện về việc tích hợp hệ thống **HubSpot CRM** vào mô hình kinh doanh D2C. Nội dung tập trung vào việc thiết kế cấu trúc vận hành, tự động hóa luồng dữ liệu và phân tích hành vi khách hàng để tối ưu hóa tăng trưởng.


## Tổng quan hệ thống
Dự án mô phỏng việc chuyển đổi quy trình quản trị từ thủ công sang hệ thống tập trung (Centralized Data). Bằng việc sử dụng bộ dữ liệu giả lập (Synthetic Data) dựa trên các chỉ số thực tế của ngành thời trang, hệ thống được thiết kế để giải quyết bài toán cá nhân hóa trải nghiệm khách hàng và tối ưu tỷ lệ chuyển đổi (CR).



## Cấu trúc Repository

### 1. [HubSpot-Full-Stack-Operations](./HubSpot-Full-Stack-Operations)
Trung tâm của kiến trúc hệ thống, bao gồm các bản vẽ kỹ thuật:
- **Data Flow:** Sơ đồ luồng luân chuyển dữ liệu từ các điểm chạm (Touchpoints) về hệ thống CRM trung tâm.
- **Workflow Automation:** Các kịch bản tự động hóa (Automated Workflows) cho Marketing Nurturing và Sales Pipeline.
- **Sales & Marketing Funnel:** Thiết kế phễu chuyển đổi tích hợp, đảm bảo sự đồng bộ giữa các bộ phận.

### 2. [lead_score_tracker](./lead_score_tracker)
Web app giả lập các quyết định khi người dùng tương tác với web Coolmate:
- **App Web Source Code:** Mã nguồn ứng dụng web giả lập hỗ trợ theo dõi và chấm điểm khách hàng tiềm năng theo thời gian thực.
- **Requirement.txt:** Danh mục các thư viện và môi trường cần thiết để vận hành ứng dụng.

### 3. [Data](./data)
Kho lưu trữ dữ liệu mô phỏng chiến dịch:
- `T0_Pre-Campaign.csv`: Dữ liệu thực trạng hệ thống trước khi triển khai MarTech.
- `T1-T6_Post-Campaign.csv`: Chuỗi dữ liệu theo dõi mức độ phát triển và hiệu quả sau chiến dịch (T0 đến T6).

### 4. [Phân tích & Thực trạng]
Các tệp phân tích chuyên sâu bằng Python:
- `COOLMATE_PRE-CAMPAIGN_ANALYTICS.ipynb`: Phân tích EDA về thực trạng hành vi khách hàng và xác định các điểm yếu trong vận hành.
- `COOLMATE_T0-T6.ipynb`: Mô hình phân tích so sánh và đánh giá mức độ tăng trưởng sau khi áp dụng hệ thống mới.

### 5. [Báo cáo]
- **Báo cáo chiến dịch Coolmate x HubSpot.pdf**: Tài liệu phân tích chi tiết về chiến lược, ngân sách và lộ trình thực thi.
- **Slide Chiến dịch Coolmate x HubSpot.pdf**: Bản trình bày tóm tắt các giá trị cốt lõi của dự án.


## Công cụ & Công nghệ vận hành
- **Nền tảng MarTech:** HubSpot (CRM, Marketing Hub, Sales Hub).
- **Ngôn ngữ phân tích:** Python (Pandas, Matplotlib, Seaborn).
- **Phát triển ứng dụng:** Python / Streamlit Framework.
- **Tư duy thiết kế:** Logic Workflow, Data Mapping & Funnel Optimization.

---
*Lưu ý: Dự án sử dụng dữ liệu giả lập nhằm mục đích nghiên cứu và minh họa giải pháp chiến lược, đảm bảo các nguyên tắc bảo mật thông tin.*
