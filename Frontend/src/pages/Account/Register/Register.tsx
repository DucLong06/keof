import { Button, Form, Input } from "antd";
import { observer } from "mobx-react-lite";
import { useEffect } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import logo from "../../../assets/media/logos/logo.svg";
import { registerStore as store } from "./RegisterStore";
type Props = {};

function useQuery() {
    return new URLSearchParams(useLocation().search);
}

const Register = observer(() => {
    const [form] = Form.useForm();
    let navigate = useNavigate();
    let query = useQuery();
    if (!query.get("code")) {
        navigate("/");
    }

    const paramData = {
        idEmail: query.get("email") || "",
        code: query.get("code") || "",
    };

    useEffect(() => {
        store.checkKey(paramData.idEmail, paramData.code);
    }, []);

    //listen to onpopstate event
    window.addEventListener("popstate", (e: any) => {
        store.registerSuccess = false;
        store.emailRegister = "";
    });

    return (
        <div className="bg-account flex justify-center items-center w-full h-full min-h-screen p-8">
            <div className="w-full max-w-100 bg-white p-8 rounded-6 shadow-md flex flex-col gap-8 items-center">
                {logo && <img src={logo} alt="logo" className="w-auto h-7" />}
                <div className="flex flex-col gap-5 w-full">
                    {paramData.idEmail === "" ? (
                        <div>
                            <h1 className="text-gray-900 text-18 font-medium mb-0">
                                Đăng ký tài khoản
                            </h1>
                            {store.registerSuccess ? (
                                <p className="mb-0">
                                    Chúng tôi đã gửi một email đến địa chỉ{" "}
                                    <b>{store.emailRegister}</b>, vui lòng xác
                                    nhận email trong vòng <b>24 giờ</b>. Cảm ơn
                                    bạn.
                                </p>
                            ) : (
                                <Form
                                    name="basic"
                                    form={form}
                                    onFinish={store.onFinish}
                                    autoComplete="off"
                                    layout="vertical"
                                >
                                    <Form.Item
                                        label="Email"
                                        name="email"
                                        rules={[
                                            {
                                                required: true,
                                                message: "Vui lòng nhập email!",
                                            },
                                            {
                                                type: "email",
                                                message:
                                                    "Email không đúng định dạng!",
                                            },
                                        ]}
                                    >
                                        <Input
                                            placeholder="Email"
                                            value={store.email}
                                            onBlur={(e: any) => {
                                                {
                                                    form.setFieldsValue({
                                                        ["email"]:
                                                            store.onEmailBlur(
                                                                e
                                                            ),
                                                    });
                                                }
                                            }}
                                        />
                                    </Form.Item>

                                    <Form.Item>
                                        <Button
                                            type="primary"
                                            htmlType="submit"
                                            loading={store.loading}
                                            block
                                        >
                                            Đăng ký tài khoản
                                        </Button>
                                    </Form.Item>
                                </Form>
                            )}
                        </div>
                    ) : (
                        <div>
                            {store.expiredLink ? (
                                <div>
                                    <h1 className="text-gray-900 text-18 font-medium mb-0">
                                        Đăng ký tài khoản thành công
                                    </h1>
                                    <span className="text-gray-900 text-18 font-medium mb-0">
                                        Vui lòng kiểm tra email để nhận mã <br>API-Key</br>
                                    </span>
                                </div>
                            ) : (
                                <p className="mb-0 flex flex-col">
                                    <div>
                                        <h1 className="text-gray-900 text-18 font-medium mb-0">
                                            Đăng ký tài khoản không thành công
                                        </h1>
                                        <span>
                                            Link xác nhận không tồn tại hoặc đã
                                            quá hạn. Vui lòng chọn đăng ký lại
                                            tài khoản tại đây.
                                        </span>
                                    </div>
                                </p>
                            )}
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
});

export default Register;
