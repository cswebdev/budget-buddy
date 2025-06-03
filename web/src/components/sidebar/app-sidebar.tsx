"use client"

import * as React from "react"
import {
  BookOpen,
  
  DollarSign,
  Frame,
  LandmarkIcon,
  LifeBuoy,
  Map,
  PieChart,
  Send,
  Settings2,

} from "lucide-react"

import { NavMain } from "@/components/sidebar/nav-main"
import { NavProjects } from "@/components/sidebar/nav-projects"
import { NavSecondary } from "@/components/sidebar/nav-secondary"
import { NavUser } from "@/components/sidebar/nav-user"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/components/sidebar/ui/sidebar"

const data = {
  user: {
    name: "default user",
    email: "blank@gmail.com",
    avatar: "/avatars/shadcn.jpg",
  },
  navMain: [
    {
      title: "Dashboard",
      url: "/dashboard",
      icon: PieChart,
    },
    {
      title: "Accounts",
      url: "#",
      icon: LandmarkIcon,
      items: [
        { title: "All Accounts", url: "#" },
        { title: "Add Account", url: "#" },
      ],
    },
    {
      title: "Transactions",
      url: "/transactions",
      icon: DollarSign,
      items: [
        { title: "All Transactions", url: "#" },
        { title: "Credit", url: "#" },
        { title: "Debit", url: "#" },
      ],
    },
    {
      title: "Financial Goals",
      url: "/goals",
      icon: Frame,
      items: [
        { title: "All Goals", url: "#" },
        { title: "Add Goal", url: "#" },
      ],
    },
    {
      title: "Reports",
      url: "#",
      icon: BookOpen,
    },
    
  ],
  navSecondary: [
   
    {
      title: "Settings",
      url: "#",
      icon: Settings2,
    },
    {
      title: "Support",
      url: "#",
      icon: LifeBuoy,
    },
    {
      title: "Feedback",
      url: "#",
      icon: Send,
    },
  ],
  projects: [
    {
      name: "Design Engineering",
      url: "#",
      icon: Frame,
    },
    {
      name: "Sales & Marketing",
      url: "#",
      icon: PieChart,
    },
    {
      name: "Travel",
      url: "#",
      icon: Map,
    },
  ],
}

export function AppSidebar({ ...props }: React.ComponentProps<typeof Sidebar>) {
  return (
    <Sidebar variant="inset" {...props}>
      <SidebarHeader>
        <SidebarMenu>
          <SidebarMenuItem>
            <SidebarMenuButton size="lg" asChild>
              <a href="#">
                <div className="bg-green-500 text-sidebar-primary-foreground flex aspect-square size-8 items-center justify-center rounded-lg">
                  <DollarSign className="size-4" />
                </div>
                <div className="grid flex-1 text-left text-sm leading-tight">
                  <span className="truncate font-bold">Budget Buddy</span>
                  <span className="truncate text-xs text-gray-600">Manage Your Finances</span>
                </div>
              </a>
            </SidebarMenuButton>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarHeader>
      <SidebarContent>
        <NavMain items={data.navMain} />
        {/* <NavProjects projects={data.projects} /> */}
        <NavSecondary items={data.navSecondary} className="mt-auto" />
      </SidebarContent>
      <SidebarFooter>
        <NavUser user={data.user} />
      </SidebarFooter>
    </Sidebar>
  )
}
