import re

with open('/Users/beexu/Documents/jmeter1/sql/1799/t_driver_apply_20190412.sql') as file_object:
    # contents = file_object.read()
    for line in file_object.readlines():
        driverapply= re.search('1120\d{3}', line)
        b300 = str(int(driverapply.group()) + 300)
        line = line.replace(driverapply.group(), str(b300))
        print(line)
        with open('/Users/beexu/Documents/jmeter1/sql/1799/t_driver_apply_test.sql', 'a+') as f:
            f.writelines([line])
            f.close()



#
# str1 ="INSERT INTO `t_driver_apply`(`driver_id`, `user_id`, `check_status`, `driver_name`, `driver_sex`, `driver_bvn`, `driver_state`, `driver_city`, `driver_address`, `driver_email`, `driver_birthplace`, `driver_ethnic`, `driver_license_date`, `driver_license_id`, `driver_license_img`, `driver_license_deadline`, `driver_front_photo`, `driver_memo`, `withdrawal_cash`, `accept_order`, `driver_birthday`) VALUES (1120200, 1800, 1, 'test_driver', 0, 'bvn21100138300', 2328926, 2332453, 'address', 'test@xgo.one', 'test', 'test', '2019-01-01', 'test', 'test', '2029-01-01', 'test', 'test', 0, 0, '1990-01-01');"
# a = re.search('1120\d{3}', str1)
# b = str(int(a.group())+300)
# # c = str1.replace(a.group(), str(b))
