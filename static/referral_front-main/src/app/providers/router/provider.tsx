import { Suspense, lazy } from "react";

import {
    createBrowserRouter,
    RouterProvider as Provider,
    Navigate
} from "react-router-dom";

import { useAuth } from "@/shared/lib/hooks/use-auth";

import { GoogleAuthenticationPage } from "@/pages/authentication/google";

import { AuthenticationLayout } from "@/pages/authentication/layout";
import { App } from "@/App";
import { AppLayout } from "@/pages/app-layout";
import { SignInPage } from "@/pages/authentication/sign-in";
import { SignUpPage } from "@/pages/sign-up-page";

const RecoverPasswordPage = lazy(async () =>
    import("@/pages/recover-password").then(module => ({
        default: module.RecoverPasswordPage
    }))
);

const RecoverPasswordConfirmPage = lazy(async () =>
    import("@/pages/recover-password-confirm").then(module => ({
        default: module.RecoverPasswordConfirmPage
    }))
);

import { StartPage } from "@/pages/start-page";

const DashboardPage = lazy(async () =>
    import("@/pages/dashboard").then(module => ({
        default: module.DashboardPage
    }))
);

const ReferralPage = lazy(async () =>
    import("@/pages/referral-page").then(module => ({
        default: module.ReferralPage
    }))
);

const SubReferralPage = lazy(async () =>
    import("@/pages/sub-referral-page").then(module => ({
        default: module.SubReferralPage
    }))
);

const StatisticPage = lazy(async () =>
    import("@/pages/statistic-page").then(module => ({
        default: module.StatisticPage
    }))
);

const CashOutPage = lazy(async () =>
    import("@/pages/cash-out-page").then(module => ({
        default: module.CashOutPage
    }))
);

const ProfilePage = lazy(async () =>
    import("@/pages/profile/page").then(module => ({
        default: module.ProfilePage
    }))
);

const publicRouter = createBrowserRouter([
    {
        path: "/",
        element: <StartPage />
    },
    {
        path: "sign",
        element: <App />,
        children: [
            {
                path: "in",
                element: <SignInPage />
            },
            {
                path: "up",
                element: <SignUpPage />
            }
        ]
    },
    {
        path: "auth",
        element: <AuthenticationLayout />,
        children: [
            {
                path: "sign/in",
                element: <SignInPage />
            }
        ]
    },
    {
        path: "password/recover",
        element: (
            <Suspense fallback={<>Loading...</>}>
                <RecoverPasswordPage />
            </Suspense>
        )
    },
    {
        path: "password/recover/confirm",
        element: (
            <Suspense fallback={<>Loading...</>}>
                <RecoverPasswordConfirmPage />
            </Suspense>
        )
    },
    {
        path: "google/complete/",
        element: <GoogleAuthenticationPage />
    },
    {
        path: "*",
        element: <Navigate to="/" />
    }
]);

const privateRouter = createBrowserRouter([
    {
        path: "/",
        element: <AppLayout />,
        children: [
            {
                index: true,
                element: (
                    <Suspense>
                        <DashboardPage />
                    </Suspense>
                )
            },
            {
                path: "/referral",
                element: (
                    <Suspense>
                        <ReferralPage />
                    </Suspense>
                )
            },
            {
                path: "/sub/referral",
                element: (
                    <Suspense>
                        <SubReferralPage />
                    </Suspense>
                )
            },
            {
                path: "/statistic",
                element: (
                    <Suspense>
                        <StatisticPage />
                    </Suspense>
                )
            },
            {
                path: "/cash/out",
                element: (
                    <Suspense>
                        <CashOutPage />
                    </Suspense>
                )
            },
            {
                path: "/profile",
                element: (
                    <Suspense>
                        <ProfilePage />
                    </Suspense>
                )
            }
        ]
    },
    {
        path: "*",
        element: <Navigate to="/" />
    }
]);

export const RouterProvider = () => {
    const { isAuthenticated } = useAuth();

    const router = isAuthenticated ? privateRouter : publicRouter;

    return <Provider router={router} />;
};
