# File chứa dữ liệu 50 ngành nghề Việt Nam
PROFESSIONS_DATA = [
    {
        'name': 'Kỹ sư phần mềm',
        'description': 'Phát triển và bảo trì các ứng dụng phần mềm',
        'skills': ['Lập trình', 'Thiết kế hệ thống', 'Giải quyết vấn đề', 'Làm việc nhóm'],
        'qualities': ['Tư duy logic', 'Kiên nhẫn', 'Sáng tạo', 'Tỉ mỉ'],
        'questions': [
            {
                'question': 'Kỹ sư phần mềm chủ yếu làm việc với cái gì?',
                'options': {'A': 'Máy cơ khí', 'B': 'Code và hệ thống', 'C': 'Các loại kim loại', 'D': 'Động vật'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Bác sĩ',
        'description': 'Chẩn đoán và điều trị bệnh cho bệnh nhân',
        'skills': ['Chẩn đoán y tế', 'Giao tiếp', 'Cấp cứu', 'Kiến thức y học'],
        'qualities': ['Trách nhiệm', 'Sự quan tâm', 'Từ bi', 'Tập trung cao độ'],
        'questions': [
            {
                'question': 'Điều quan trọng nhất đối với một bác sĩ là gì?',
                'options': {'A': 'Tiền lương cao', 'B': 'Chăm sóc sức khỏe bệnh nhân', 'C': 'Thời gian rảnh', 'D': 'Danh tiếng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Giáo viên',
        'description': 'Giảng dạy và truyền tải kiến thức cho học sinh',
        'skills': ['Giảng dạy', 'Quản lý lớp', 'Giao tiếp', 'Tạo nội dung'],
        'qualities': ['Kiên nhẫn', 'Đam mê', 'Trách nhiệm', 'Sáng tạo'],
        'questions': [
            {
                'question': 'Vai trò chính của giáo viên là gì?',
                'options': {'A': 'Kiếm tiền', 'B': 'Truyền kiến thức và phát triển học sinh', 'C': 'Cho học sinh làm bài tập', 'D': 'Viết sách'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Kế toán',
        'description': 'Quản lý tài chính và ghi chép tài khoản',
        'skills': ['Tính toán', 'Phân tích tài chính', 'Sử dụng phần mềm', 'Chú ý chi tiết'],
        'qualities': ['Tính chính xác', 'Tổ chức tốt', 'Tâm cẩn thận', 'Tin cậy'],
        'questions': [
            {
                'question': 'Kế toán làm việc chủ yếu với cái gì?',
                'options': {'A': 'Máy móc', 'B': 'Người lao động', 'C': 'Dữ liệu tài chính', 'D': 'Vật liệu xây dựng'},
                'correct_answer': 'C'
            }
        ]
    },
    {
        'name': 'Kỹ sư xây dựng',
        'description': 'Thiết kế và quản lý dự án xây dựng',
        'skills': ['Thiết kế', 'Tính toán kỹ thuật', 'Quản lý dự án', 'CAD'],
        'qualities': ['Tư duy không gian', 'Trách nhiệm', 'Lãnh đạo', 'Chính xác'],
        'questions': [
            {
                'question': 'Kỹ sư xây dựng chủ yếu tham gia vào giai đoạn nào?',
                'options': {'A': 'Thiết kế và quản lý thi công', 'B': 'Bán hàng', 'C': 'Nấu ăn', 'D': 'Y tế'},
                'correct_answer': 'A'
            }
        ]
    },
    {
        'name': 'Nhân viên kinh doanh',
        'description': 'Phát triển mối quan hệ và bán sản phẩm/dịch vụ',
        'skills': ['Giao tiếp bán hàng', 'Thương lượng', 'Xây dựng mối quan hệ', 'Thuyết phục'],
        'qualities': ['Năng động', 'Kiên trì', 'Tự tin', 'Thích chở chất'],
        'questions': [
            {
                'question': 'Kỹ năng quan trọng nhất của nhân viên kinh doanh là gì?',
                'options': {'A': 'Biết nấu ăn', 'B': 'Giao tiếp và thuyết phục khách hàng', 'C': 'Biết chơi nhạc', 'D': 'Thể thao'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Họa sĩ',
        'description': 'Tạo các tác phẩm nghệ thuật bằng các phương tiện khác nhau',
        'skills': ['Vẽ vời', 'Sáng tạo', 'Thiết kế', 'Thẩm mỹ'],
        'qualities': ['Sáng tạo', 'Tưởng tượng', 'Khéo léo', 'Dành cơ'],
        'questions': [
            {
                'question': 'Điều gì là cần thiết nhất cho một họa sĩ?',
                'options': {'A': 'Máy tính', 'B': 'Sáng tạo và tưởng tượng', 'C': 'Kiến thức toán học', 'D': 'Khả năng nấu ăn'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Lập trình viên',
        'description': 'Viết code để phát triển ứng dụng và phần mềm',
        'skills': ['Lập trình', 'Giải quyết vấn đề', 'Debuging', 'Hiểu cấu trúc dữ liệu'],
        'qualities': ['Tư duy logic', 'Kiên nhẫn', 'Tập trung', 'Sáng tạo'],
        'questions': [
            {
                'question': 'Lập trình viên cần có kỹ năng nào?',
                'options': {'A': 'Hát hay', 'B': 'Viết code và giải quyết vấn đề', 'C': 'Chơi thể thao', 'D': 'Vẽ tranh'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Thiết kế đồ họa',
        'description': 'Tạo các thiết kế trực quan cho in ấn, web, và phương tiện',
        'skills': ['Thiết kế', 'Sáng tạo', 'Sử dụng phần mềm', 'Thẩm mỹ'],
        'qualities': ['Tưởng tượng', 'Thẩm mỹ', 'Sáng tạo', 'Chú ý chi tiết'],
        'questions': [
            {
                'question': 'Thiết kế đồ họa làm việc chủ yếu với cái gì?',
                'options': {'A': 'Máy móc nặng', 'B': 'Hình ảnh và thiết kế trực quan', 'C': 'Động vật', 'D': 'Cây cối'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Quản lý nhân sự',
        'description': 'Quản lý nhân lực, tuyển dụng, và phát triển sự nghiệp nhân viên',
        'skills': ['Giao tiếp', 'Quản lý con người', 'Giải quyết tranh chấp', 'Tuyển dụng'],
        'qualities': ['Sự đồng cảm', 'Công bằng', 'Tổ chức tốt', 'Khôn ngoan'],
        'questions': [
            {
                'question': 'Vai trò chính của quản lý nhân sự là gì?',
                'options': {'A': 'Nấu ăn cho nhân viên', 'B': 'Quản lý nhân viên và phát triển đội ngũ', 'C': 'Vẽ tranh', 'D': 'Bán sản phẩm'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Kỹ sư điện',
        'description': 'Thiết kế và bảo trì các hệ thống điện',
        'skills': ['Kỹ thuật điện', 'Giải quyết vấn đề', 'CAD', 'Tiêu chuẩn an toàn'],
        'qualities': ['Chính xác', 'Cẩn thận', 'Tư duy kỹ thuật', 'Trách nhiệm'],
        'questions': [
            {
                'question': 'Kỹ sư điện làm việc chủ yếu với cái gì?',
                'options': {'A': 'Nước', 'B': 'Hệ thống điện', 'C': 'Đá', 'D': 'Gỗ'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Y tá',
        'description': 'Hỗ trợ bác sĩ trong chăm sóc bệnh nhân',
        'skills': ['Chăm sóc bệnh nhân', 'Giao tiếp', 'Kiến thức y tế', 'Kỹ năng đặc biệt y tế'],
        'qualities': ['Từ bi', 'Kiên nhẫn', 'Trách nhiệm', 'Tập trung'],
        'questions': [
            {
                'question': 'Y tá cần có tính chất nào?',
                'options': {'A': 'Bướng bỉnh', 'B': 'Từ bi và kiên nhẫn', 'C': 'Lười biếng', 'D': 'Nóng tính'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhà báo',
        'description': 'Thu thập thông tin và viết bài báo',
        'skills': ['Viết lách', 'Phỏng vấn', 'Tìm kiếm tin tức', 'Giao tiếp'],
        'qualities': ['Tò mò', 'Chính trực', 'Giao tiếp tốt', 'Tư duy phản biện'],
        'questions': [
            {
                'question': 'Nhà báo chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Thu thập và viết tin tức', 'C': 'Xây dựng', 'D': 'Chữa bệnh'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Luật sư',
        'description': 'Cung cấp tư vấn pháp lý và bảo vệ quyền lợi',
        'skills': ['Kiến thức pháp luật', 'Lập luận', 'Giao tiếp', 'Nghiên cứu'],
        'qualities': ['Tư duy logic', 'Chính trực', 'Lẫn lộn', 'Khôn ngoan'],
        'questions': [
            {
                'question': 'Vai trò của luật sư là gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Cung cấp tư vấn pháp lý', 'C': 'Vẽ tranh', 'D': 'Chơi thể thao'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Mỹ phẩm',
        'description': 'Làm đẹp và chăm sóc da, tóc, móng',
        'skills': ['Mỹ phẩm', 'Tạo kiểu', 'Giao tiếp', 'Sáng tạo'],
        'qualities': ['Sáng tạo', 'Tỉ mỉ', 'Thích xã hội', 'Khéo léo'],
        'questions': [
            {
                'question': 'Chuyên gia mỹ phẩm làm việc chủ yếu với cái gì?',
                'options': {'A': 'Máy móc', 'B': 'Ngoại hình con người', 'C': 'Cây cối', 'D': 'Động vật'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Đầu bếp',
        'description': 'Chuẩn bị và nấu các món ăn',
        'skills': ['Nấu ăn', 'Quản lý nhà bếp', 'Vệ sinh thực phẩm', 'Sáng tạo menu'],
        'qualities': ['Sáng tạo', 'Khéo léo', 'Tổ chức tốt', 'Kỹ thuật cao'],
        'questions': [
            {
                'question': 'Đầu bếp cần có kỹ năng nào?',
                'options': {'A': 'Lập trình', 'B': 'Nấu ăn và quản lý nhà bếp', 'C': 'Vẽ tranh', 'D': 'Xây dựng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Quản lý dự án',
        'description': 'Lên kế hoạch và giám sát thực hiện dự án',
        'skills': ['Lập kế hoạch', 'Quản lý', 'Giao tiếp', 'Giải quyết vấn đề'],
        'qualities': ['Tổ chức tốt', 'Lãnh đạo', 'Tư duy chiến lược', 'Quyết đoán'],
        'questions': [
            {
                'question': 'Quản lý dự án chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Lên kế hoạch và giám sát dự án', 'C': 'Chơi thể thao', 'D': 'Viết thơ'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhà khoa học',
        'description': 'Tiến hành nghiên cứu khoa học',
        'skills': ['Nghiên cứu', 'Phân tích', 'Thử nghiệm', 'Toán học'],
        'qualities': ['Tò mò', 'Tư duy phản biện', 'Kiên trì', 'Chính xác'],
        'questions': [
            {
                'question': 'Nhà khoa học làm việc chủ yếu với cái gì?',
                'options': {'A': 'Mây', 'B': 'Nghiên cứu và thí nghiệm', 'C': 'Sóng nước', 'D': 'Gió'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Marketing',
        'description': 'Xây dựng chiến lược tiếp thị và quảng cáo',
        'skills': ['Tiếp thị', 'Phân tích dữ liệu', 'Sáng tạo', 'Giao tiếp'],
        'qualities': ['Sáng tạo', 'Tư duy chiến lược', 'Thích chạy rủi ro', 'Năng động'],
        'questions': [
            {
                'question': 'Marketing chủ yếu tập trung vào cái gì?',
                'options': {'A': 'Y tế', 'B': 'Quảng cáo và chiến lược bán hàng', 'C': 'Xây dựng', 'D': 'Nông nghiệp'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Kỹ sư cơ khí',
        'description': 'Thiết kế và sản xuất máy móc',
        'skills': ['Thiết kế cơ khí', 'CAD', 'Sản xuất', 'Giải quyết vấn đề'],
        'qualities': ['Tư duy kỹ thuật', 'Chính xác', 'Tổ chức tốt', 'Sáng tạo'],
        'questions': [
            {
                'question': 'Kỹ sư cơ khí làm việc chủ yếu với cái gì?',
                'options': {'A': 'Các loại cây', 'B': 'Máy móc và cơ khí', 'C': 'Các loại cá', 'D': 'Mây'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhân viên kế toán ngân hàng',
        'description': 'Quản lý tài chính tại các ngân hàng',
        'skills': ['Kế toán', 'Tài chính', 'Tiền tệ', 'Phần mềm ngân hàng'],
        'qualities': ['Tính chính xác', 'Tin cậy', 'Tổ chức tốt', 'Bảo mật cao'],
        'questions': [
            {
                'question': 'Nhân viên ngân hàng cần tính chất nào?',
                'options': {'A': 'Bất cẩn', 'B': 'Chính xác và tin cậy', 'C': 'Lười biếng', 'D': 'Bốc đồng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Thợ cắt tóc',
        'description': 'Cắt tóc và tạo kiểu tóc cho khách hàng',
        'skills': ['Cắt tóc', 'Tạo kiểu', 'Giao tiếp', 'Sáng tạo'],
        'qualities': ['Khéo léo', 'Thích xã hội', 'Sáng tạo', 'Cẩn thận'],
        'questions': [
            {
                'question': 'Thợ cắt tóc cần có kỹ năng nào?',
                'options': {'A': 'Lập trình', 'B': 'Cắt tóc và tạo kiểu', 'C': 'Xây dựng', 'D': 'Nông nghiệp'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Phân tích dữ liệu',
        'description': 'Phân tích dữ liệu để đưa ra quyết định kinh doanh',
        'skills': ['Phân tích', 'SQL', 'Python', 'Thống kê'],
        'qualities': ['Tư duy logic', 'Chính xác', 'Tập trung', 'Giải quyết vấn đề'],
        'questions': [
            {
                'question': 'Phân tích dữ liệu làm việc chủ yếu với cái gì?',
                'options': {'A': 'Nước', 'B': 'Dữ liệu và thống kê', 'C': 'Gỗ', 'D': 'Cây cối'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Thợ điện',
        'description': 'Lắp đặt và sửa chữa hệ thống điện',
        'skills': ['Kỹ thuật điện', 'Lắp đặt', 'Sửa chữa', 'An toàn'],
        'qualities': ['Khéo léo', 'Cẩn thận', 'Chặt chẽ', 'Trách nhiệm'],
        'questions': [
            {
                'question': 'Thợ điện chủ yếu làm việc với cái gì?',
                'options': {'A': 'Nước', 'B': 'Điện và hệ thống điện', 'C': 'Cây cối', 'D': 'Động vật'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhân viên bán lẻ',
        'description': 'Bán hàng và phục vụ khách tại các cửa hàng',
        'skills': ['Giao tiếp', 'Bán hàng', 'Phục vụ khách hàng', 'Quản lý thời gian'],
        'qualities': ['Thân thiện', 'Kiên nhẫn', 'Năng động', 'Xã hội'],
        'questions': [
            {
                'question': 'Nhân viên bán lẻ cần tính chất nào?',
                'options': {'A': 'Thô ơi', 'B': 'Thân thiện và kiên nhẫn', 'C': 'Lười biếng', 'D': 'Tự cao tự đại'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Kỹ sư hóa học',
        'description': 'Phát triển quá trình hóa học và sản phẩm',
        'skills': ['Hóa học', 'Quy trình', 'Thí nghiệm', 'Kiến thức kỹ thuật'],
        'qualities': ['Tư duy khoa học', 'Chính xác', 'Cẩn thận', 'Sáng tạo'],
        'questions': [
            {
                'question': 'Kỹ sư hóa học làm việc chủ yếu với cái gì?',
                'options': {'A': 'Hóa chất và quy trình hóa học', 'B': 'Cây cối', 'C': 'Động vật', 'D': 'Nước'},
                'correct_answer': 'A'
            }
        ]
    },
    {
        'name': 'Nhiếp ảnh gia',
        'description': 'Chụp ảnh để lưu giữ khoảnh khắc',
        'skills': ['Chụp ảnh', 'Sáng tạo', 'Chỉnh sửa ảnh', 'Thẩm mỹ'],
        'qualities': ['Tư duy thẩm mỹ', 'Sáng tạo', 'Tập trung', 'Kiên nhẫn'],
        'questions': [
            {
                'question': 'Nhiếp ảnh gia chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Chụp ảnh và chỉnh sửa', 'C': 'Xây dựng', 'D': 'Lập trình'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Hướng dẫn viên du lịch',
        'description': 'Hướng dẫn khách du lịch qua các địa điểm',
        'skills': ['Giao tiếp', 'Kiến thức địa lý', 'Hướng dẫn', 'Ngoại ngữ'],
        'qualities': ['Thân thiện', 'Năng động', 'Kiến thức rộng', 'Xã hội'],
        'questions': [
            {
                'question': 'Hướng dẫn viên du lịch cần có kỹ năng nào?',
                'options': {'A': 'Lập trình', 'B': 'Giao tiếp và kiến thức địa lý', 'C': 'Nấu ăn', 'D': 'Y tế'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Tiếp lễ',
        'description': 'Tiếp đón và hỗ trợ khách hàng',
        'skills': ['Giao tiếp', 'Tiếp khách', 'Tổ chức', 'Chú ý chi tiết'],
        'qualities': ['Thân thiện', 'Chuyên nghiệp', 'Tổ chức tốt', 'Kiên nhẫn'],
        'questions': [
            {
                'question': 'Tiếp lễ chủ yếu làm gì?',
                'options': {'A': 'Lập trình', 'B': 'Tiếp đón và hỗ trợ khách', 'C': 'Nấu ăn', 'D': 'Xây dựng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhân viên CNTT',
        'description': 'Quản lý công nghệ thông tin và hỗ trợ kỹ thuật',
        'skills': ['IT', 'Mạng', 'Hỗ trợ kỹ thuật', 'Bảo mật'],
        'qualities': ['Giải quyết vấn đề', 'Kiên nhẫn', 'Tư duy kỹ thuật', 'Tổ chức tốt'],
        'questions': [
            {
                'question': 'Nhân viên CNTT cần có kỹ năng nào?',
                'options': {'A': 'Nấu ăn', 'B': 'IT và hỗ trợ kỹ thuật', 'C': 'Vẽ tranh', 'D': 'Chơi thể thao'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Thư ký',
        'description': 'Hỗ trợ quản lý hành chính và lịch biểu',
        'skills': ['Giao tiếp', 'Tổ chức', 'Viết lách', 'Quản lý thời gian'],
        'qualities': ['Tổ chức tốt', 'Cẩn thận', 'Tin cậy', 'Kiên nhẫn'],
        'questions': [
            {
                'question': 'Thư ký chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Hỗ trợ quản lý hành chính', 'C': 'Xây dựng', 'D': 'Nông nghiệp'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Lái xe',
        'description': 'Lái xe để vận chuyển hành khách hoặc hàng hóa',
        'skills': ['Lái xe', 'An toàn đường bộ', 'Sửa chữa cơ bản', 'Giao tiếp'],
        'qualities': ['Cẩn thận', 'Tỉnh táo', 'Trách nhiệm', 'Kiên nhẫn'],
        'questions': [
            {
                'question': 'Lái xe cần có tính chất nào?',
                'options': {'A': 'Bốc đồng', 'B': 'Cẩn thận và tỉnh táo', 'C': 'Lười biếng', 'D': 'Thô ơi'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Kiến trúc sư',
        'description': 'Thiết kế các công trình kiến trúc',
        'skills': ['Thiết kế', 'CAD', 'Thẩm mỹ', 'Tính toán'],
        'qualities': ['Sáng tạo', 'Tư duy không gian', 'Thẩm mỹ', 'Chính xác'],
        'questions': [
            {
                'question': 'Kiến trúc sư làm việc chủ yếu với cái gì?',
                'options': {'A': 'Máy tính', 'B': 'Thiết kế công trình', 'C': 'Nước', 'D': 'Động vật'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhà môi giới bất động sản',
        'description': 'Tìm kiếm và bán bất động sản cho khách hàng',
        'skills': ['Bán hàng', 'Giao tiếp', 'Kiến thức bất động sản', 'Thương lượng'],
        'qualities': ['Năng động', 'Tự tin', 'Kiên trì', 'Thích chạy rủi ro'],
        'questions': [
            {
                'question': 'Nhà môi giới bất động sản chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Bán và cho thuê bất động sản', 'C': 'Lập trình', 'D': 'Y tế'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Thợ xây',
        'description': 'Thực hiện công việc xây dựng',
        'skills': ['Xây dựng', 'Kỹ năng tay', 'An toàn', 'Đọc bản vẽ'],
        'qualities': ['Khéo léo', 'Chăm chỉ', 'Cẩn thận', 'Mạnh khỏe'],
        'questions': [
            {
                'question': 'Thợ xây chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Thực hiện công việc xây dựng', 'C': 'Lập trình', 'D': 'Giảng dạy'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Chuyên viên pháp lý',
        'description': 'Cung cấp tư vấn pháp lý chuyên sâu',
        'skills': ['Pháp luật', 'Nghiên cứu', 'Lập luận', 'Tư duy logic'],
        'qualities': ['Tư duy logic', 'Chính trực', 'Cẩn thận', 'Kiên trì'],
        'questions': [
            {
                'question': 'Chuyên viên pháp lý cần có kỹ năng nào?',
                'options': {'A': 'Nấu ăn', 'B': 'Pháp luật và tư duy logic', 'C': 'Vẽ tranh', 'D': 'Chơi thể thao'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhân viên quản lý kho',
        'description': 'Quản lý kho và hàng hóa',
        'skills': ['Quản lý kho', 'Tổ chức', 'Đếm hàng', 'Phần mềm kho'],
        'qualities': ['Tổ chức tốt', 'Chính xác', 'Cẩn thận', 'Trách nhiệm'],
        'questions': [
            {
                'question': 'Nhân viên quản lý kho cần tính chất nào?',
                'options': {'A': 'Bất cẩn', 'B': 'Tổ chức tốt và chính xác', 'C': 'Lười biếng', 'D': 'Bốc đồng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhà thiết kế thời trang',
        'description': 'Thiết kế và tạo các bộ sưu tập thời trang',
        'skills': ['Thiết kế thời trang', 'Sáng tạo', 'May mặc', 'Thẩm mỹ'],
        'qualities': ['Sáng tạo', 'Thẩm mỹ', 'Tưởng tượng', 'Khéo léo'],
        'questions': [
            {
                'question': 'Nhà thiết kế thời trang làm việc với cái gì?',
                'options': {'A': 'Máy móc', 'B': 'Vải và thiết kế', 'C': 'Cây cối', 'D': 'Động vật'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Huấn luyện viên thể thao',
        'description': 'Hướng dẫn và huấn luyện vận động viên',
        'skills': ['Huấn luyện', 'Kiến thức thể thao', 'Giao tiếp', 'Động lực'],
        'qualities': ['Năng động', 'Trách nhiệm', 'Khích lệ', 'Kiên trì'],
        'questions': [
            {
                'question': 'Huấn luyện viên thể thao chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Huấn luyện vận động viên', 'C': 'Lập trình', 'D': 'Vẽ tranh'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhân viên tiếp tân',
        'description': 'Tiếp đón và xử lý yêu cầu khách hàng',
        'skills': ['Giao tiếp', 'Tiếp đón', 'Tổ chức', 'Ngoại ngữ'],
        'qualities': ['Thân thiện', 'Chuyên nghiệp', 'Kiên nhẫn', 'Xã hội'],
        'questions': [
            {
                'question': 'Nhân viên tiếp tân cần có tính chất nào?',
                'options': {'A': 'Thô ơi', 'B': 'Thân thiện và chuyên nghiệp', 'C': 'Lười biếng', 'D': 'Bốc đồng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhà báo chuyên ngành',
        'description': 'Viết về các chủ đề chuyên biệt',
        'skills': ['Viết lách', 'Phỏng vấn', 'Nghiên cứu', 'Giao tiếp'],
        'qualities': ['Tò mò', 'Chính trực', 'Tư duy phân tích', 'Viết giỏi'],
        'questions': [
            {
                'question': 'Nhà báo chuyên ngành chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Viết về chủ đề chuyên biệt', 'C': 'Xây dựng', 'D': 'Y tế'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Chuyên gia môi trường',
        'description': 'Bảo vệ và quản lý môi trường',
        'skills': ['Khoa học môi trường', 'Phân tích', 'Nghiên cứu', 'Quy pháp'],
        'qualities': ['Quan tâm đến thiên nhiên', 'Trách nhiệm', 'Tư duy khoa học', 'Kiên trì'],
        'questions': [
            {
                'question': 'Chuyên gia môi trường làm việc với cái gì?',
                'options': {'A': 'Máy móc', 'B': 'Bảo vệ và quản lý môi trường', 'C': 'Vải', 'D': 'Tài chính'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Chuyên viên marketing số',
        'description': 'Quản lý các chiến dịch tiếp thị trực tuyến',
        'skills': ['Digital marketing', 'SEO', 'Social media', 'Phân tích dữ liệu'],
        'qualities': ['Sáng tạo', 'Tư duy chiến lược', 'Thích công nghệ', 'Năng động'],
        'questions': [
            {
                'question': 'Chuyên viên marketing số làm việc chủ yếu với cái gì?',
                'options': {'A': 'Nước', 'B': 'Tiếp thị trực tuyến', 'C': 'Gỗ', 'D': 'Đá'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Lập trình viên web',
        'description': 'Phát triển các ứng dụng web',
        'skills': ['HTML/CSS', 'JavaScript', 'Backend', 'Database'],
        'qualities': ['Tư duy logic', 'Sáng tạo', 'Kiên nhẫn', 'Học hỏi'],
        'questions': [
            {
                'question': 'Lập trình viên web chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Phát triển ứng dụng web', 'C': 'Vẽ tranh', 'D': 'Y tế'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Quản lý bán hàng',
        'description': 'Quản lý đội bán hàng và đạt chỉ tiêu bán',
        'skills': ['Quản lý', 'Bán hàng', 'Lãnh đạo', 'Phân tích'],
        'qualities': ['Lãnh đạo', 'Năng động', 'Tự tin', 'Quyết đoán'],
        'questions': [
            {
                'question': 'Quản lý bán hàng chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Quản lý đội bán hàng', 'C': 'Lập trình', 'D': 'Xây dựng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhân viên khảo sát',
        'description': 'Tiến hành khảo sát và thu thập dữ liệu',
        'skills': ['Phỏng vấn', 'Giao tiếp', 'Tổ chức', 'Nhập liệu'],
        'qualities': ['Tò mò', 'Kiên nhẫn', 'Chính xác', 'Xã hội'],
        'questions': [
            {
                'question': 'Nhân viên khảo sát chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Tiến hành khảo sát', 'C': 'Lập trình', 'D': 'Xây dựng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhà soạn nhạc',
        'description': 'Sáng tác các bản nhạc',
        'skills': ['Sáng tác', 'Hiểu nhạc lý', 'Công cụ âm nhạc', 'Sáng tạo'],
        'qualities': ['Sáng tạo', 'Tưởng tượng', 'Nhạy cảm', 'Kiên trì'],
        'questions': [
            {
                'question': 'Nhà soạn nhạc chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Sáng tác bản nhạc', 'C': 'Lập trình', 'D': 'Xây dựng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhân viên an ninh',
        'description': 'Bảo vệ an ninh tại các cơ sở',
        'skills': ['Bảo vệ', 'Giao tiếp', 'Cảnh báo', 'Tâm lý'],
        'qualities': ['Cảnh báo', 'Dũng cảm', 'Trách nhiệm', 'Tỉnh táo'],
        'questions': [
            {
                'question': 'Nhân viên an ninh cần có tính chất nào?',
                'options': {'A': 'Lười biếng', 'B': 'Cảnh báo và dũng cảm', 'C': 'Bất cẩn', 'D': 'Bốc đồng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Chuyên gia thương mại điện tử',
        'description': 'Quản lý các hoạt động bán hàng trực tuyến',
        'skills': ['E-commerce', 'Digital marketing', 'Quản lý cửa hàng', 'Phân tích'],
        'qualities': ['Sáng tạo', 'Tư duy chiến lược', 'Thích công nghệ', 'Năng động'],
        'questions': [
            {
                'question': 'Chuyên gia thương mại điện tử làm việc với cái gì?',
                'options': {'A': 'Nước', 'B': 'Bán hàng trực tuyến', 'C': 'Gỗ', 'D': 'Động vật'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhân viên hành chính',
        'description': 'Hỗ trợ các công việc hành chính',
        'skills': ['Hành chính', 'Tổ chức', 'Giao tiếp', 'Quản lý tài liệu'],
        'qualities': ['Tổ chức tốt', 'Chính xác', 'Cẩn thận', 'Trách nhiệm'],
        'questions': [
            {
                'question': 'Nhân viên hành chính chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Hỗ trợ công việc hành chính', 'C': 'Lập trình', 'D': 'Xây dựng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhạc sĩ',
        'description': 'Biểu diễn và sáng tác nhạc',
        'skills': ['Chơi nhạc cụ', 'Sáng tạo', 'Biểu diễn', 'Đọc nhạc'],
        'qualities': ['Sáng tạo', 'Nhạy cảm', 'Kiên trì', 'Kỹ năng'],
        'questions': [
            {
                'question': 'Nhạc sĩ chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Biểu diễn và sáng tác nhạc', 'C': 'Lập trình', 'D': 'Y tế'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Bác sĩ nha khoa',
        'description': 'Chăm sóc sức khỏe rặng và yếm',
        'skills': ['Nha khoa', 'Điều trị răng', 'Giao tiếp', 'Kỹ thuật'],
        'qualities': ['Trách nhiệm', 'Khéo léo', 'Cẩn thận', 'Sự quan tâm'],
        'questions': [
            {
                'question': 'Bác sĩ nha khoa chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Chăm sóc sức khỏe răng', 'C': 'Lập trình', 'D': 'Xây dựng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Dược sĩ',
        'description': 'Chuẩn bị và bán thuốc',
        'skills': ['Dược học', 'Giao tiếp', 'Cân nhắc', 'Kỹ thuật'],
        'qualities': ['Chính xác', 'Trách nhiệm', 'Cẩn thận', 'Tin cậy'],
        'questions': [
            {
                'question': 'Dược sĩ chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Chuẩn bị và bán thuốc', 'C': 'Lập trình', 'D': 'Xây dựng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Thực tập sinh',
        'description': 'Học tập và thực hành tại doanh nghiệp',
        'skills': ['Học tập', 'Giao tiếp', 'Thực hành', 'Thích nghi'],
        'qualities': ['Say mê học hỏi', 'Khiêm tốn', 'Kiên nhẫn', 'Tò mò'],
        'questions': [
            {
                'question': 'Thực tập sinh chủ yếu làm gì?',
                'options': {'A': 'Làm việc chỉnh nghiêm', 'B': 'Học tập và thực hành', 'C': 'Nấu ăn', 'D': 'Xây dựng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Chuyên gia tuyển dụng',
        'description': 'Tuyển dụng và phỏng vấn ứng viên',
        'skills': ['Phỏng vấn', 'Tuyển dụng', 'Giao tiếp', 'Đánh giá'],
        'qualities': ['Tư duy phê bình', 'Công bằng', 'Giao tiếp tốt', 'Sự đồng cảm'],
        'questions': [
            {
                'question': 'Chuyên gia tuyển dụng chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Tuyển dụng và phỏng vấn ứng viên', 'C': 'Lập trình', 'D': 'Xây dựng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhân viên sửa chữa',
        'description': 'Sửa chữa và bảo trì các thiết bị',
        'skills': ['Sửa chữa', 'Khéo léo', 'Kiến thức kỹ thuật', 'Giải quyết vấn đề'],
        'qualities': ['Khéo léo', 'Tư duy kỹ thuật', 'Kiên nhẫn', 'Cẩn thận'],
        'questions': [
            {
                'question': 'Nhân viên sửa chữa chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Sửa chữa và bảo trì thiết bị', 'C': 'Lập trình', 'D': 'Xây dựng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhà quản lý sản xuất',
        'description': 'Quản lý quy trình sản xuất',
        'skills': ['Quản lý', 'Sản xuất', 'Quy trình', 'Kiểm chất'],
        'qualities': ['Tổ chức tốt', 'Lãnh đạo', 'Hiệu quả', 'Quyết đoán'],
        'questions': [
            {
                'question': 'Nhà quản lý sản xuất chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Quản lý quy trình sản xuất', 'C': 'Lập trình', 'D': 'Y tế'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Chuyên gia lương thực',
        'description': 'Quản lý và phát triển sản phẩm lương thực',
        'skills': ['Nông nghiệp', 'Kiến thức lương thực', 'Phân tích', 'Quy trình'],
        'qualities': ['Trách nhiệm', 'Kiên trì', 'Tư duy khoa học', 'Quan tâm chất lượng'],
        'questions': [
            {
                'question': 'Chuyên gia lương thực làm việc với cái gì?',
                'options': {'A': 'Máy móc', 'B': 'Sản phẩm lương thực', 'C': 'Vải', 'D': 'Tài chính'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhà phân tích kinh tế',
        'description': 'Phân tích xu hướng kinh tế và đưa dự báo',
        'skills': ['Kinh tế học', 'Phân tích', 'Thống kê', 'Dự báo'],
        'qualities': ['Tư duy logic', 'Chính xác', 'Tập trung', 'Học hỏi'],
        'questions': [
            {
                'question': 'Nhà phân tích kinh tế chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Phân tích kinh tế', 'C': 'Lập trình', 'D': 'Xây dựng'},
                'correct_answer': 'B'
            }
        ]
    },
    {
        'name': 'Nhân viên logistic',
        'description': 'Quản lý vận chuyển và kho bãi',
        'skills': ['Logistic', 'Vận chuyển', 'Quản lý', 'Tính toán'],
        'qualities': ['Tổ chức tốt', 'Hiệu quả', 'Cẩn thận', 'Trách nhiệm'],
        'questions': [
            {
                'question': 'Nhân viên logistic chủ yếu làm gì?',
                'options': {'A': 'Nấu ăn', 'B': 'Quản lý vận chuyển và kho bãi', 'C': 'Lập trình', 'D': 'Y tế'},
                'correct_answer': 'B'
            }
        ]
    }
]
