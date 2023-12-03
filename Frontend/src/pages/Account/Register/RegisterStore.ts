import { makeAutoObservable } from "mobx";
import axiosClient from "../../../utils/apis/RequestHelper";
import { _IApiResponse } from "../../../utils/interfaces/IApiResponse";

interface IRegister {
    email: string;
}

class RegisterStore {
    registerSuccess: boolean = false;
    emailRegister: string = "";
    loading: boolean = false;
    email: string = "";
    idEmail: string = "";
    code: string = "";
    expiredLink: boolean = false;

    constructor() {
        makeAutoObservable(this)
    }
    register = async (data: IRegister): Promise<_IApiResponse> => {
        return axiosClient.post("api/accounts/register/", data);
    }

    checkSecretKey = async (idEmail: string, code: string): Promise<_IApiResponse> => {
        return axiosClient.get(`/api/accounts/validate-token/?email=${idEmail}&code=${code}`);
    }

    onFinish = async (data: any) => {
        try {
            this.loading = true;
            const response = await this.register({
                ...data,
            });

            this.loading = false;
            if (response.status === 200) {
                this.registerSuccess = true;
                this.emailRegister = data.email;
            }
            else if (response.status === 201) {
                this.registerSuccess = true;
                this.emailRegister = data.email;
            }

        } catch (e) {
            console.log("Failed: ", e);
        }

    }

    onEmailBlur = (e: any) => {
        return e.target.value.trim()
    }

    checkKey = async (idEmail: string, code: string) => {
        if (idEmail !== "" && code !== "") {
            try {
                const response = await this.checkSecretKey(idEmail, code);
                if (response.status === 200) {
                    this.idEmail = idEmail
                    this.code = code
                    this.expiredLink = true;
                }
                else {
                    
                }
            } catch (error) {
                console.log(error);
            }
        }
    }

}

export const registerStore = new RegisterStore()
