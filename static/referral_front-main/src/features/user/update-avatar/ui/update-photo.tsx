import { useUpdateUserPhotoMutation } from "@/entities/user/api";
import { FetchUserData } from "@/entities/user/ui/fetch";
import { cnBase } from "tailwind-variants";

interface UpdateUserPhotoFormProps
    extends React.ComponentPropsWithoutRef<"label"> {}

// function readFileAsBase64(file) {
//     return new Promise((resolve, reject) => {
//         const reader = new FileReader();
//         reader.onload = () => resolve(reader?.result.split(",")[1]);
//         reader.onerror = error => reject(error);
//         reader.readAsDataURL(file);
//     });
// }

export const UpdateUserPhotoForm: React.FC<UpdateUserPhotoFormProps> = ({
    className,
    ...props
}) => {
    const [updateUserPhoto] = useUpdateUserPhotoMutation();

    const onChangeHandler: React.FormEventHandler<
        HTMLInputElement
    > = async event => {
        const { files } = event.currentTarget;

        if (!files || files.length === 0) return;

        const img = files[0];

        try {
            await updateUserPhoto(img).unwrap();
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <FetchUserData
            renderSuccess={({ photo }) => (
                <label
                    className={cnBase("cursor-pointer", className)}
                    {...props}
                >
                    <img
                        src={`${import.meta.env.VITE_BASE_API_URL}${photo}`}
                        alt="User photo"
                        className="size-48 rounded-full border-4 border-violet-primary object-cover"
                    />
                    <span className="sr-only">Update user avatar</span>
                    <input
                        type="file"
                        name="photo"
                        accept="image/*"
                        onChange={onChangeHandler}
                        hidden
                    />
                </label>
            )}
            loadingFallback={
                <div className="size-48 animate-pulse place-content-center rounded-full border-4 border-violet-primary bg-slate-400" />
            }
        />
    );
};
