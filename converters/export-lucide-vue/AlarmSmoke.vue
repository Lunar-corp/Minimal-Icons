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
    <path d="M4 8a2 2 0 0 1-2-2V3h20v3a2 2 0 0 1-2 2Z" />
    <path d="m19 8-.8 3c-.1.6-.6 1-1.2 1H7c-.6 0-1.1-.4-1.2-1L5 8" />
    <path d="M16 21c0-2.5 2-2.5 2-5" />
    <path d="M11 21c0-2.5 2-2.5 2-5" />
    <path d="M6 21c0-2.5 2-2.5 2-5" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>