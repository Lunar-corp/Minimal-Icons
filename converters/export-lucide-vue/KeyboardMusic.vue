<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    :stroke-width="stroke"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <rect width="20" height="16" x="2" y="4" rx="2" />
    <path d="M6 8h4" />
    <path d="M14 8h.01" />
    <path d="M18 8h.01" />
    <path d="M2 12h20" />
    <path d="M6 12v4" />
    <path d="M10 12v4" />
    <path d="M14 12v4" />
    <path d="M18 12v4" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>