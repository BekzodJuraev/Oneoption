import "styled-components";
import { ThemeType } from "@/app/styles/themes/default-theme";

declare module "styled-components" {
    export interface DefaultTheme extends ThemeType {}
}
